from fastapi import APIRouter

from .models import RawProductIn, ProductOut, ScrapedProductIn
from .services import normalize_product, normalize_scraped_product

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/normalize", response_model=ProductOut)
def normalize_product_route(product: RawProductIn):
    return normalize_product(product)


@router.post("/normalize-scraped", response_model=ProductOut)
def normalize_scraped_product_route(product: ScrapedProductIn):
    return normalize_scraped_product(product)