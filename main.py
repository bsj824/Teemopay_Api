"""
入口文件
"""
import pytest
import os

if __name__ == '__main__':
    # pytest.main(["-vs", "./test_case/test_payout.py"])
    pytest.main(["-vs", "./test_case/test_payout.py","--alluredir", "./result", "--clean-alluredir"])
    os.system("allure generate ./result -o ./report_allure --clean")
