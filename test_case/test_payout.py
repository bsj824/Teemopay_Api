# import allure
import jsonpath
import pytest
from config import *
import json
import logging
from api_key.api_key import ApiKey


# @allure.step("创建代收订单")
# def test_01_payout(get_Authorization):
#     api_key = get_Authorization
#     url = "https://test-mx-gateway.teemopay.com/api/pay/payment/create/v1"
#
#     payload = json.dumps({
#         "merchantOrderNo": "o1t9j3s8x93k512txm268at219v30a01",
#         "realName": "XinXu",
#         "amount": "1000",
#         "callbackUrl": "https://sandbox.presimex.mx/api/user/public/teemopay/payment/callback/78f04feca0c5581628508b156d364fc0",
#         "paymentType": 1,
#         "email": "1015922891@qq.com",
#         "phone": "13175025808",
#         "sign": "QRcD1SNmv9SEQJSJX47fsbfsVDG5hbdg+K/cb3Wa12EBeJR+MTwx0emuBvAxWLQ53tu3QNj0jQAGPInEoCDAJi7TpaIJwtXxtLqGc/elMD/5j6TE3KAWINt5uREGonY8XSesaF7HO63yFuDAd6DBi0a/wYF1eK2eyUQyJC6aeS4="
#     })
#     headers = {
#         'timestamp': '1709102586001',
#         'nonce': 'jHVtrauIf364QdDRwwrBuFISISyyY6UC',
#         'country': 'MX',
#         'app_code': 'A2404010004MX001',
#         'Content-Type': 'application/json'
#     }
#     res = api_key.post(url=url, headers=headers, data=payload)
#     print(res.text)


def test_03_platformSuccessRate(get_authorization):
    """
    获取通道成功率接口
    :return:
    """
    # api_key, authorization = get_authorization
    api_key=get_authorization
    # print(api_key, authorization)
    authorization = TOKEN
    url = "https://test-crm.teemopay.com/api/manage/MX/platform/pay/platformSuccessRate"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': authorization
    }
    payload = json.dumps({
        "startTime": "2024-05-05 00:00:00",
        "endTime": "2024-05-05 23:59:59",
        "page": 1,
        "size": 20,
        "type": 2
    })
    res = api_key.post(url=url, headers=headers, data=payload)
    code = api_key.get_text(res.text, "$..code")
