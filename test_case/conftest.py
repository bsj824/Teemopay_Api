import json
import logging
import pytest

from api_key.api_key import ApiKey
from config import *


@pytest.fixture(scope='session')
def get_authorization():
    """
    获取token
    :return: 返回token
    """
    api_key = ApiKey()
    # url = PLATFORM_URL+"api/global/login"
    # headers = {
    #     'Content-Type': 'application/json'
    # }
    # payload = json.dumps({
    #     "googleCode": "983629",  # google验证码
    #     "username": "baoshoujia0810@gmail.com",  # 账号
    #     "password": "12345Qaz"  # 密码
    # })
    # res = api_key.post(url=url, headers=headers, data=payload)
    # authorization = api_key.get_text(res.json(), '$..authorization')
    # return api_key, authorization[0]
    return api_key


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # out 调用这个方法的case返回过来的一个对象
    out = yield
    # 类似于return ，返回，但是它的区别是当调用它的方法结束之后，返回到当前位置
    res = out.get_result()
    if res.when == "call":
        logging.info(f"用例ID：{res.nodeid}")
        logging.info(f"测试结果：{res.outcome}")
        logging.info(f"故障表示：{res.longrepr}")
        logging.info(f"异常：{call.excinfo}")
        logging.info(f"用例耗时：{res.duration}")
        logging.info("**************************************")