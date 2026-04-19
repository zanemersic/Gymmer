from backend.api.nutrition.providers.openfoodfacts_client import OpenFoodFactsClient
from backend.api.nutrition.providers.usda_client import USDAClient


class NutritionService:
    def __init__(self):
        self.openfoodfacts = OpenFoodFactsClient()
        self.usda = USDAClient()

    def get_product_by_barcode(self, barcode: str):
        product = self.openfoodfacts.get_by_barcode(barcode)

        if not product:
            return None

        return self.clean_openfoodfacts_product(product, barcode)

    def search_foods(self, query: str, page_size: int = 10):
        data = self.usda.search_foods(query, page_size)

        return [
            self.clean_usda_food(food)
            for food in data.get("foods", [])
        ]

    def clean_openfoodfacts_product(self, product: dict, barcode: str):
        nutriments = product.get("nutriments", {})

        return {
            "source": "OpenFoodFacts",
            "barcode": barcode,
            "name": product.get("product_name"),
            "brand": product.get("brands"),
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
        }

    def clean_usda_food(self, food: dict):
        nutrients = {
            item.get("nutrientName"): item.get("value")
            for item in food.get("foodNutrients", [])
        }

        return {
            "source": "USDA",
            "fdc_id": food.get("fdcId"),
            "name": food.get("description"),
            "brand": food.get("brandOwner"),
            "data_type": food.get("dataType"),
            "nutrition_per_100g": {
                "energy_kcal": nutrients.get("Energy"),
                "protein": nutrients.get("Protein"),
                "carbohydrates": nutrients.get("Carbohydrate, by difference"),
                "fat": nutrients.get("Total lipid (fat)"),
                "fiber": nutrients.get("Fiber, total dietary"),
                "sugars": nutrients.get("Sugars, total including NLEA"),
                "sodium": nutrients.get("Sodium, Na"),
            },
        }