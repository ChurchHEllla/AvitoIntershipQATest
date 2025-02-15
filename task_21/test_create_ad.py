import pytest
from client import ApiClient
import config as co

# Получение базового идентификатора продавца из конфигурационного файла
baseSellerID = co.baseSellerID
# Фикстура для создания клиента
@pytest.fixture
def api_client():    
    return ApiClient()

def test_1(api_client):
    request_data = {
        "sellerID": baseSellerID,
        "name": "mashroom",
        "price": 530,
        "statistics": {
            "contacts": 54,
            "likes": 145,
            "viewCount": 2989
        }
    }
    # Отправка запроса на создание объявления
    api_client.create_ad(request_data)

    # Проверка статуса ответа
    assert api_client.response.status_code == 200, f"Ожидалось получение статуса 200 ок, но набор данных прошел неуспешно"

def test_2(api_client):
    request_data = {
        "sellerID": baseSellerID,
        "name": "mashroom",
        "price": 530,
    }
    api_client.create_ad(request_data)
    assert api_client.response.status_code == 200, f"Ожидалось получение статуса 200 ок, но набор данных прошел неуспешно"


    # # Проверка наличия идентификатора в ответе
    # response_data = api_client.response.json()
    # assert "id" in response_data, "Expected 'id' in response, but it was not found"

    # # Вывод идентификатора созданного объявления
    # print(f"Created ad ID: {response_data['id']}")

@pytest.mark.parametrize(
    "pNData, pReqData", 
    [
        (1,{
            "sellerID": baseSellerID,
            "name": "bee",
        }),
         (2,{
            "sellerID": baseSellerID,
            "price": 50,
        }),
         (3,{
            "name": "bee",
            "price": 50,
        })
    ])
def test_3(api_client, pNData, pReqData):
    request_data = pReqData
    message = pNData

    api_client.create_ad(request_data)
    assert api_client.response.status_code == 400, f"Ожидалось получение статуса 400 Bad Request и сообщение об ошибке, но  набор данных {message} прошел успешно"



@pytest.mark.parametrize(
    "pNData, pSellerID, pName, pPrice, pContacts, pLikes, pViewCount",
    [
        (1, -baseSellerID, "toy", 2000, 50, 300, 1500),  
        (2, baseSellerID, "toy", -2000, 50, 300, 1500), 
        (3, baseSellerID, "toy", 2000, -50, 300, 1500), 
        (4, baseSellerID, "toy", 2000, 50, -300, 1500), 
        (5, baseSellerID, "toy", 2000, 50, -300, -1500)
    ]
)
def test_4( api_client, pNData, pSellerID, pName, pPrice, pContacts, pLikes, pViewCount):
    request_data = {
        "sellerID": pSellerID,
        "name": pName,
        "price": pPrice,
        "statistics": {
            "contacts": pContacts,
            "likes": pLikes,
            "viewCount": pViewCount
        }
    }
    message = pNData
    api_client.create_ad(request_data)
    assert api_client.response.status_code == 400, f"Ожидалось получение статуса 400 Bad Request и сообщение об ошибке, но  набор данных {message} прошел успешно"

@pytest.mark.parametrize(
"pNData, pSellerID, pName, pPrice, pContacts, pLikes, pViewCount",
[
    (1,'Charmander', "toy", 2000, 50, 300, 1500),  
    (2, baseSellerID, 677, -2000, 50, 300, 1500), 
    (3, baseSellerID, "toy", 2000, 'Charmander', 300, 1500), 
    (4, baseSellerID, "toy", 2000, 50, 'Charmander', 1500), 
    (5, baseSellerID, "toy", 2000, 50, -300, 'Charmander')
]
)
def test_5( api_client, pNData, pSellerID, pName, pPrice, pContacts, pLikes, pViewCount):
    request_data = {
        "sellerID": pSellerID,
        "name": pName,
        "price": pPrice,
        "statistics": {
            "contacts": pContacts,
            "likes": pLikes,
            "viewCount": pViewCount
        }
    }
    message = pNData
    api_client.create_ad(request_data)
    assert api_client.response.status_code == 400, f"Ожидалось получение статуса 400 Bad Request и сообщение об ошибке, но  набор данных {message} прошел успешно"