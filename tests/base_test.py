import pytest
from pages.login_page import LoginPage
from pages.customer_login_page import CustomerLoginPage
from pages.account_page import Account
from pages.transactions_page import Transaction

class BaseTest:

    login_page : LoginPage
    customer_login_page : CustomerLoginPage
    account_page : Account
    transactions_page : Transaction

    @pytest.fixture(autouse=True)
    def setup(self,request,driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.customer_login_page = CustomerLoginPage(driver)
        request.cls.account_page = Account(driver)
        request.cls.transactions_page = Transaction(driver)