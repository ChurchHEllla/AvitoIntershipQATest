import pytest
from client import ApiClient
import config as co

baseSellerID = co.baseSellerID

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

    api_client.create_ad(request_data)

    assert api_client.response.status_code == 200, f"Ожидалось получение статуса 200 ок, но запрос прошел неуспешно"

def test_2(api_client):
    request_data = {
        "sellerID": baseSellerID,
        "name": "mashroom",
        "price": 530,
    }
    api_client.create_ad(request_data)

    assert api_client.response.status_code == 200, f"Ожидалось получение статуса 200 ок, но запрос прошел неуспешно"


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

    assert api_client.response.status_code == 400, f"Ожидалось получение статуса 400 Bad Request и сообщение об ошибке, но  запрос {message} прошел успешно"



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

    assert api_client.response.status_code == 400, f"Ожидалось получение статуса 400 Bad Request и сообщение об ошибке, но  запрос {message} прошел успешно"

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

    assert api_client.response.status_code == 400, f"Ожидалось получение статуса 400 Bad Request и сообщение об ошибке, но  запрос {message} прошел успешно"