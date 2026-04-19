from fastapi import APIRouter, HTTPException, Query
from backend.api.nutrition.service import NutritionService

router = APIRouter(
    prefix="/api/nutrition",
    tags=["Nutrition"]
)

service = NutritionService()


@router.get("/products/{barcode}")
def get_product_by_barcode(barcode: str):
    product = service.get_product_by_barcode(barcode)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.get("/search")
def search_foods(
    query: str = Query(..., min_length=2),
    page_size: int = Query(default=10, ge=1, le=50)
):
    return {
        "query": query,
        "results": service.search_foods(query, page_size)
    }