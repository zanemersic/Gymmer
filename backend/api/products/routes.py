from fastapi import APIRouter

from .models import RawProductIn, ProductOut
from .services import normalize_product

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/normalize", response_model=ProductOut)
def normalize_product_route(product: RawProductIn):
    return normalize_product(product)