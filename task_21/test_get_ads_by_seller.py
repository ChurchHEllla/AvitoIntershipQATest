import pytest
from client import ApiClient 
from data_reader import JsonToDict
@pytest.fixture
def api_client():    
    return ApiClient()

def test_9(api_client):
    dataReader = JsonToDict("./data/data_test_9.json")
    testData = dataReader.data[0]
    print(testData)
    api_client.get_ads_by_seller(878788)
    assert api_client.response.status_code == 200, f"Ожидалось получение статуса 200 ок, но запрос прошел неуспешно"

    if api_client.response.status_code == 200:
        data = api_client.response.json()[0]

        assert 'id' in data, "В ответе отсутствует поле 'id'"
        assert data["id"] == testData["id"], f"ID объявления в ответе не совпадает с ожидаемым: {testData["id"]}"
        assert "name" in data, "В ответе отсутствует поле 'name'"
        assert "price" in data, "В ответе отсутствует поле 'price'"
        assert "contacts" in data["statistics"], "В ответе отсутствует поле 'contacts'"
        assert "likes" in data["statistics"], "В ответе отсутствует поле 'likes'"
        assert "viewCount" in data["statistics"], "В ответе отсутствует поле 'viewCount'"
     

        assert isinstance(data["name"], str), "Поле 'name' должно быть строкой"
        assert isinstance(data["price"], (int, float)), "Поле 'price' должно быть числом"
        assert isinstance(data["statistics"]["contacts"], int), "Поле 'contacts' должно быть целым числом"
        assert isinstance(data["statistics"]["likes"], int), "Поле 'likes' должно быть целым числом"
        assert isinstance(data["statistics"]["viewCount"], int), "Поле 'viewCount' должно быть целым числом"
       
        assert data["name"] == testData["name"], f"Имя объявления в ответе не совпадает с ожидаемым: {testData['name']}"
        assert data["price"] == testData["price"], f"Цена объявления в ответе не совпадает с ожидаемой: {testData['price']}"
        assert data["statistics"]["contacts"] == testData["statistics"]["contacts"], f"Количество контактов в ответе не совпадает с ожидаемым: {testData['contacts']}"
        assert data["statistics"]["likes"] == testData["statistics"]["likes"], f"Количество лайков в ответе не совпадает с ожидаемым: {testData['likes']}"
        assert data["statistics"]["viewCount"] == testData["statistics"]["viewCount"], f"Количество просмотров в ответе не совпадает с ожидаемым: {testData['views']}"

def test_10(api_client):
    dataReader = JsonToDict("./data/data_test_9.json")
    testData = dataReader.data[0]
    print(testData)
    api_client.get_ads_by_seller(878789)

    assert api_client.response.status_code == 404, f"Ожидалось получение статуса 404 Not Founded, но запрос прошел успешно"


def test_11(api_client):
    dataReader = JsonToDict("./data/data_test_9.json")
    testData = dataReader.data[0]
    print(testData)
    api_client.get_ads_by_seller("picapicaaa")

    assert api_client.response.status_code == 400, f"Ожидалось получение статуса 400 Bad Request, но запрос прошел успешно"
