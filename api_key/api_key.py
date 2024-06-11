"""
工具类，实现关键字封装文件
"""

import requests
import jsonpath
import json
# import allure


class ApiKey:
    # @allure.step("--get请求---")
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    # @allure.step("--post请求---")
    def post(self, url, data=None, json=None, **kwargs):
        return requests.post(url=url, data=data, json=json, **kwargs)

    # @allure.step("--获取响应数据，判断字符串---")
    def get_text(self, response_data, json_path):
        # 判断response_data是否是字符串
        if isinstance(response_data, str):
            json.loads(response_data)
        return jsonpath.jsonpath(response_data, json_path)
