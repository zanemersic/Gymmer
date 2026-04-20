from typing import Optional, Dict
from pydantic import BaseModel, Field


class NutritionPer100g(BaseModel):
    calories_kcal: Optional[float] = Field(default=None, ge=0)
    protein_g: Optional[float] = Field(default=None, ge=0)
    carbohydrates_g: Optional[float] = Field(default=None, ge=0)
    sugars_g: Optional[float] = Field(default=None, ge=0)
    fat_g: Optional[float] = Field(default=None, ge=0)
    saturated_fat_g: Optional[float] = Field(default=None, ge=0)
    fiber_g: Optional[float] = Field(default=None, ge=0)
    salt_g: Optional[float] = Field(default=None, ge=0)


class ProductSource(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None


class RawProductIn(BaseModel):
    name: str = Field(..., min_length=1)
    brand: Optional[str] = None
    barcode: Optional[str] = None
    quantity: Optional[str] = None
    source: Optional[ProductSource] = None
    nutrition_per_100g: NutritionPer100g


class ScrapedProductIn(BaseModel):
    url: str
    ime_izdelka: str
    hranilne_vrednosti: Dict[str, str] = Field(default_factory=dict)


class ProductOut(BaseModel):
    id: Optional[str] = None
    name: str
    brand: Optional[str] = None
    barcode: Optional[str] = None
    quantity: Optional[str] = None
    nutrition_per_100g: NutritionPer100g
    source: Optional[ProductSource] = None