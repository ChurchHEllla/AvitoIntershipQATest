import pytest
from client import ApiClient 
from data_reader import JsonToDict
@pytest.fixture
def api_client():    
    return ApiClient()

@pytest.mark.parametrize(
    "pNData, pItemId", [
    (1, "740d3f07-aa41-4dd5-823e-4c032c0454e6"),
    (2, "b7852ee5-4033-43b6-aed8-d622719ce2d7"),
    (3, "46460b09-e8e3-437e-afa4-cb05d56e5de0"),
    ])

def test_12(api_client, pNData, pItemId):
    dataReader = JsonToDict("./data/data_test_12.json")
    testData = dataReader.getElementById("id", pItemId)
    api_client.get_statistics(pItemId)
    assert api_client.response.status_code == 200, f"Ожидалось получение статуса 200 ok, но запрос прошел неуспешно"

    if api_client.response.status_code == 200:
        data = api_client.response.json()[0]

        assert "contacts" in data, "В ответе отсутствует поле 'contacts'"
        assert "likes" in data, "В ответе отсутствует поле 'likes'"
        assert "viewCount" in data, "В ответе отсутствует поле 'viewCount'"
     

        assert isinstance(data["contacts"], int), "Поле 'contacts' должно быть целым числом"
        assert isinstance(data["likes"], int), "Поле 'likes' должно быть целым числом"
        assert isinstance(data["viewCount"], int), "Поле 'viewCount' должно быть целым числом"
       
        assert data["contacts"] == testData["statistics"]["contacts"], f"Количество контактов в ответе не совпадает с ожидаемым: {testData["statistics"]['contacts']}"
        assert data["likes"] == testData["statistics"]["likes"], f"Количество лайков в ответе не совпадает с ожидаемым: {testData["statistics"]['likes']}"
        assert data["viewCount"] == testData["statistics"]["viewCount"], f"Количество просмотров в ответе не совпадает с ожидаемым: {testData["statistics"]['views']}"

def test_13(api_client):
    api_client.get_statistics("b7852ee5-4033-43b6-aed8-d622700ce2d7")

    assert api_client.response.status_code == 404, f"Ожидалось получение статуса 404 Not Found, но запрос прошел успешно"

def test_14(api_client):
    api_client.get_statistics("chupapimunyanya")

    assert api_client.response.status_code == 400, f"Ожидалось получение статуса 400 Bad Request, но запрос прошел успешно"

