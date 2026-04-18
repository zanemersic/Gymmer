from fastapi import APIRouter, HTTPException
from backend.api.nutrition_client import NutritionClient

router = APIRouter(
    prefix="/api/nutrition",
    tags=["Nutrition"]
)

client = NutritionClient()

def clean_product(product: dict, barcode: str):
    nutriments = product.get("nutriments", {})

    return {
        "barcode": barcode,
        "name": product.get("product_name"),
        "brand": product.get("brands"),
        "quantity": product.get("quantity"),
        "categories": product.get("categories"),
        "image_url": product.get("image_url"),
        "nutrition_per_100g": {
            "energy_kcal": nutriments.get("energy-kcal_100g"),
            "protein": nutriments.get("proteins_100g"),
            "carbohydrates": nutriments.get("carbohydrates_100g"),
            "sugars": nutriments.get("sugars_100g"),
            "fat": nutriments.get("fat_100g"),
            "saturated_fat": nutriments.get("saturated-fat_100g"),
            "fiber": nutriments.get("fiber_100g"),
            "salt": nutriments.get("salt_100g"),
        },
        "source": "OpenFoodFacts"
    }


@router.get("/products/{barcode}")
def get_product_by_barcode(barcode: str):
    product = client.get_product_by_barcode(barcode)

    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with barcode {barcode} not found"
        )

    return clean_product(product, barcode)