# 🏋️‍♂️ Gymmer: Fitnes Spremljevalec

**Gymmer** je celovita rešitev za upravljanje telesne pripravljenosti in zdravja. Namesto uporabe ločenih aplikacij za štetje kalorij, sledenje teku in iskanje receptov, Gymmer združuje vse te funkcionalnosti v eno povezano izkušnjo z uporabo sodobnih tehnologij strganja podatkov (scraping) in oblačnih storitev.

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![React Native](https://img.shields.io/badge/Frontend-React%20Native-61DAFB?logo=react)
![Node.js](https://img.shields.io/badge/Backend-Node.js-339933?logo=node.js)
![Python](https://img.shields.io/badge/Scraper-Python-3776AB?logo=python)
![MongoDB](https://img.shields.io/badge/Database-MongoDB%20Atlas-47A248?logo=mongodb)

---

## 🌟 Ključne Funkcionalnosti

### 🍎 Prehranski Modul (UPC Scanner & Scraper)

- **Skeniranje črtnih kod:** Takojšnje prepoznavanje živil preko UPC kode.
- **Pametni Scraper:** Python API v realnem času pridobi makrohranila in kalorije iz virov, kot so OpenFoodFacts in spletne trgovine.
- **Lokalni Cache:** Podatki se shranjujejo v MongoDB za takojšen dostop prihodnjim uporabnikom.

### 🏃‍♂️ Aktivnostni Modul (GPS & Zemljevidi)

- **Sledenje teku:** Uporaba GPS senzorja za beleženje poti v realnem času.
- **OpenStreetMap (OSM):** Izris poti na zemljevidu z uporabo knjižnic Leaflet ali MapLibre.
- **Metrike:** Izračun tempa (pace), razdalje in porabljenih kalorij glede na parametre uporabnika.
- **Integracija zdravja:** Povezava z Google Fit / Apple HealthKit za štetje korakov.

### 🥗 Receptni Modul

- **Avtomatsko zbiranje:** Python scraper periodično zbira zdrave recepte s fitnes portalov.
- **Kategorizacija:** Iskanje receptov glede na vsebnost beljakovin, veganske možnosti ali čas priprave.
- **Povezava z dnevnikom:** Enostavno dodajanje obrokov iz receptov neposredno v dnevni vnos.

### 👥 Socialni Modul

- **Skupnost:** Iskanje prijateljev in pošiljanje prošenj.
- **Časovnica (Feed):** Objave zaključenih treningov in doseženih ciljev.
- **Deljenje:** Generiranje slik statistike teka za socialna omrežja (Instagram/FB).

---

## 🏗 Tehnična Arhitektura

| Komponenta          | Tehnologija                                      |
| :------------------ | :----------------------------------------------- |
| **Frontend**        | React Native (iOS & Android), React (Web)        |
| **Backend**         | Node.js (Express) & Python (za scraping module)  |
| **Podatkovna baza** | MongoDB Atlas (dokumentna baza za fleksibilnost) |
| **Zemljevidi**      | OpenStreetMap (OSM)                              |
| **Lokacija**        | GeoJSON format za shranjevanje poti              |

---

## 🚀 Razvojni Načrt (Roadmap)

- [ ] **1. faza: MVP (Minimum Viable Product)**
  - Postavitev MongoDB Atlas baze.
  - Razvoj API-ja za UPC skeniranje in osnovni prehranski dnevnik.
- [ ] **2. faza: Aktivnost in Zemljevidi**
  - Implementacija GPS sledenja in OSM integracija.
  - Shranjevanje in vizualizacija zgodovine treningov.
- [ ] **3. faza: Socializacija in Recepti**
  - Sistem za prijatelje in časovnico.
  - Integracija scraperja za recepte.
- [ ] **4. faza: Optimizacija**
  - Izboljšanje UI/UX (temni način, animacije).
  - Napredna tedenska in mesečna analitika napredka.

---

## 🛠 Namestitev in Lokalni Razvoj

1. **Kloniranje repozitorija:**

   ```bash
   git clone https://github.com/zanemersic/gymmer.git
   cd gymmer
   ```

2. **Backend API Setup:**

   Backend API uporablja **Python + FastAPI**.

   #### First-time setup:

   ```bash
    cp .env.example .env
    # Fill in required environment variables in .env

    python -m venv .venv
    source .venv/bin/activate

    pip install -r requirements.txt

    python -m uvicorn backend.api.main:app --reload
   ```

   For Windows PowerShell, activate venv with:

   ```powershell
    .venv\Scripts\Activate.ps1
   ```

   #### Later usage:

   ```bash
    git pull

    source .venv/bin/activate

    pip install -r requirements.txt

    python -m uvicorn backend.api.main:app --reload
   ```

   API will run locally at:

   ```bash
    http://127.0.0.1:8000
   ```

   FastAPI docs:

   ```bash
    http://127.0.0.1:8000/docs
   ```

3. **Frontend Setup:**
   ```bash
    cd frontend
    npm install
    npx expo start
   ```

---

### ⚠️ Izzivi in Rešitve

- **Poraba baterije:** Optimizacija osveževanja GPS lokacije med tekom.

- **Zakonitost strganja:** Spoštovanje robots.txt datotek na ciljnih spletnih mestih.

- **Točnost podatkov:** Implementacija sistema za popravljanje podatkov s strani uporabnikov (crowdsourcing).

---

**Avtorji:**

- Žan Emeršič
- Luka Marinič
- Žiga Varl

---

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
