import requests
import config

# Определяем класс ApiClient, который будет использоваться для выполнения запросов к API
class ApiClient:
    
    # Инициализируем объект класса с указанием базового URL из конфигурационного файла
    def __init__(self, base_url = config.base_url):
        self.base_url = base_url
        self.response = None
    # Метод для создания объявления  
    def create_ad(self, data):
            url = f"{self.base_url}/api/1/item"
            self.response = requests.post(url, json=data)
            return self.response
    
    # Метод для получения объявления по ID
    def get_ad_by_id(self, ad_id):
        url = f"{self.base_url}/api/1/item/{ad_id}"
        self.response = requests.get(url)
        return self.response
    
    # Метод для получения объявлений продавца по ID продавца
    def get_ads_by_seller(self, seller_id):
        url = f"{self.base_url}/api/1/{seller_id}/item"
        self.response = requests.get(url)
        return self.response
    
    # Метод для получения статистики объявления по ID объявления
    def get_statistics(self, item_id):
        url = f"{self.base_url}/api/1/statistic/{item_id}"
        self.response = requests.get(url)
        return self.response