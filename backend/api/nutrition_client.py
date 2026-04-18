import os
from dotenv import load_dotenv
from openfoodfacts import API, APIVersion, Country, Environment, Flavor

load_dotenv()

class NutritionClient:
    def __init__(self):
        self.api = API(
            user_agent="FERI-Data-Analysis-Student-Project/0.1 (contact: luka.marinic@student.um.si)",
            username=os.getenv("OFF_USERNAME"),
            password=os.getenv("OFF_PASSWORD"),
            country=Country.world,
            flavor=Flavor.off,
            version=APIVersion.v2,
            environment=Environment.org,
        )

    def get_product_by_barcode(self, barcode: str):
        product = self.api.product.get(barcode)

        if not product:
            return None

        return product