from .models import RawProductIn, ProductOut, ScrapedProductIn, NutritionPer100g, ProductSource


def clean_string(value: str | None) -> str | None:
    if value is None:
        return None

    cleaned = value.strip()
    return cleaned if cleaned else None


def parse_float(value: str | None) -> float | None:
    if value is None:
        return None

    try:
        return float(str(value).replace(",", ".").strip())
    except ValueError:
        return None


def normalize_product(product: RawProductIn) -> ProductOut:
    data = product.model_dump()

    data["name"] = data["name"].strip()
    data["brand"] = clean_string(data.get("brand"))
    data["barcode"] = clean_string(data.get("barcode"))
    data["quantity"] = clean_string(data.get("quantity"))

    return ProductOut(**data)


def normalize_scraped_product(product: ScrapedProductIn) -> ProductOut:
    values = product.hranilne_vrednosti

    return ProductOut(
        name=product.ime_izdelka.strip(),
        brand=None,
        barcode=None,
        quantity=None,
        source=ProductSource(
            name="tus.si",
            url=product.url
        ),
        nutrition_per_100g=NutritionPer100g(
            calories_kcal=parse_float(values.get("ENERGIJSKA VREDNOST V KCAL / 100G")),
            protein_g=parse_float(values.get("BELJAKOVINE NA 100G")),
            carbohydrates_g=parse_float(values.get("OGLJIKOVI HIDRATI NA 100G")),
            sugars_g=parse_float(values.get("OD TEGA SLADKORJI NA 100G")),
            fat_g=parse_float(values.get("MAŠČOBE NA 100G")),
            saturated_fat_g=parse_float(values.get("OD TEGA NASIČENE MAŠČOBE NA 100G")),
            fiber_g=parse_float(values.get("PREHRANSKE VLAKNINE NA 100G")),
            salt_g=parse_float(values.get("SOL NA 100G")),
        )
    )