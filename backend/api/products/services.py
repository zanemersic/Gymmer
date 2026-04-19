from .models import RawProductIn, ProductOut

def clean_string(value: str | None) -> str | None:
    if value is None:
        return None

    cleaned = value.strip()
    return cleaned if cleaned else None

def normalize_product(product: RawProductIn) -> ProductOut:
    data = product.model_dump()

    data["name"] = data["name"].strip()
    data["brand"] = clean_string(data.get("brand"))
    data["barcode"] = clean_string(data.get("barcode"))
    data["quantity"] = clean_string(data.get("quantity"))

    return ProductOut(**data)