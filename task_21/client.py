import requests
import config

class ApiClient:
    def __init__(self, base_url = config.base_url):
        self.base_url = base_url
        self.response = None
    def create_ad(self, data):
        url = f"{self.base_url}/api/1/item"
        self.response = requests.post(url, json=data)
        return self.response

    def get_ad_by_id(self, ad_id):
        url = f"{self.base_url}/api/1/item/{ad_id}"
        self.response = requests.get(url)
        return self.response

    def get_ads_by_seller(self, seller_id):
        url = f"{self.base_url}/api/1/{seller_id}/item"
        self.response = requests.get(url)
        return self.response

    def get_statistics(self, item_id):
        url = f"{self.base_url}/api/1/statistic/{item_id}"
        self.response = requests.get(url)
        return self.response