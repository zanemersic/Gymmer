import os
import requests
from dotenv import load_dotenv

load_dotenv()


class USDAClient:
    BASE_URL = "https://api.nal.usda.gov/fdc/v1"

    def __init__(self):
        self.api_key = os.getenv("USDA_API_KEY")

        if not self.api_key:
            raise ValueError("Missing USDA_API_KEY in .env")

    def search_foods(self, query: str, page_size: int = 10):
        response = requests.get(
            f"{self.BASE_URL}/foods/search",
            params={
                "api_key": self.api_key,
                "query": query,
                "pageSize": page_size,
            },
            timeout=10,
        )

        response.raise_for_status()
        return response.json()