import requests
from bs4 import BeautifulSoup
import time
import json

def praskaj_vse_strani_in_hranilne_vrednosti():
    # Headerji, da nas strežnik ne blokira
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    vse_povezave_izdelkov = set()
    trenutna_stran = 1
    
    print("=== KORAK 1: Iskanje izdelkov s filtri (Hrana in pijača) ===")
    
    while True:
        # URL vsebuje vse tvoje izbrane filtre iz kategorij
        url_strani = f"https://www.tus.si/aktualno/akcijska-ponudba/aktualno-iz-kataloga/page/{trenutna_stran}/?swoof=1&product_cat_m=zamrznjeno%2Csladko-in-slano%2Calkoholne-pijace%2Cbrezalkoholne-pijace%2Chlajeni-in-mlecni-izdelki%2Ckruh-in-pekovski-izdelki%2Cmednarodna-hrana%2Cmeso-delikatesa-in-ribe%2Csadje-in-zelenjava%2Cshramba"
        
        odgovor = requests.get(url_strani, headers=headers)
        
        if odgovor.status_code != 200:
            print(f"Stran {trenutna_stran} ne obstaja več. Končujem iskanje povezav.")
            break
            
        soup = BeautifulSoup(odgovor.text, 'html.parser')
        najdeni_na_tej_strani = 0
        
        for a_znacka in soup.find_all('a', href=True):
            href = a_znacka['href']
            if 'https://www.tus.si/izdelki/' in href:
                stari_count = len(vse_povezave_izdelkov)
                vse_povezave_izdelkov.add(href)
                if len(vse_povezave_izdelkov) > stari_count:
                    najdeni_na_tej_strani += 1
                    
        if najdeni_na_tej_strani == 0:
            break
            
        print(f"Najdeno {najdeni_na_tej_strani} izdelkov na strani {trenutna_stran}.")
        trenutna_stran += 1
        time.sleep(0.5)

    povezave_seznam = list(vse_povezave_izdelkov)
    print(f"\nSkupaj najdenih {len(povezave_seznam)} unikatnih izdelkov. Začenjam praskanje hranilnih vrednosti...")
    
    vsi_podatki = []

    for index, url in enumerate(povezave_seznam, 1):
        print(f"[{index}/{len(povezave_seznam)}] Obdelujem: {url}")
        
        try:
            odgovor_izdelka = requests.get(url, headers=headers)
            soup_izdelka = BeautifulSoup(odgovor_izdelka.text, 'html.parser')
            
            podatki_izdelka = {
                "url": url,
                "ime_izdelka": "Neznano",
                "hranilne_vrednosti": {}
            }
            
            h1 = soup_izdelka.find('h1')
            if h1:
                podatki_izdelka["ime_izdelka"] = h1.text.strip()
                
            tabele = soup_izdelka.find_all('table')
            for tabela in tabele:
                for vrstica in tabela.find_all('tr'):
                    celice = vrstica.find_all(['td', 'th'])
                    if len(celice) == 2:
                        kljuc = celice[0].text.strip()
                        vrednost = celice[1].text.strip()
                        if kljuc and vrednost:
                            podatki_izdelka["hranilne_vrednosti"][kljuc] = vrednost
            
            vsi_podatki.append(podatki_izdelka)
            
        except Exception as e:
            print(f"Napaka pri izdelku {url}: {e}")
            
        time.sleep(0.5)
        # Test: procesira samo en izdelek za testiranje API integracije
        break
        
    return vsi_podatki

if __name__ == "__main__":
    # Zaženemo praskanje
    rezultati = praskaj_vse_strani_in_hranilne_vrednosti()
    
    print("\nObdelava končana.")

    #  POŠILJANJA NA API:
    # print("Pošiljam podatke na API...")
    # api_url = "https://tvoja-domena.com/api/vnos-hrane"
    # odgovor_api = requests.post(api_url, json=rezultati) 
    # print(f"Status odgovora API: {odgovor_api.status_code}")
    
    # Izpis v konzolo za testiranje (samo prvih nekaj, da ne zasmetimo ekrana)
    if rezultati:
        print("\nPrimer prvega izdelka:")
        print(json.dumps(rezultati[0], indent=4, ensure_ascii=False))

        api_url = "http://127.0.0.1:8000/products/normalize-scraped"

        odgovor_api = requests.post(api_url, json=rezultati[0])

        print(f"Status odgovora API: {odgovor_api.status_code}")
        print(json.dumps(odgovor_api.json(), indent=4, ensure_ascii=False))