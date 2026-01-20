from tests.base_test import BaseTest
import allure
import pytest

@allure.feature('Profile func')
class TestProfileFeature(BaseTest):

    @allure.title("test")
    @allure.severity('Critical')
    @pytest.mark.smoke
    def test_balance(self):
        self.login_page.open()
        self.login_page.login_customer()
        self.customer_login_page.is_opened()
        self.customer_login_page.choice_name()
        self.customer_login_page.login_customer_page()
        self.account_page.is_opened()
        self.account_page.click_on_deposit()
        self.account_page.click_on_amount_of_deposit()
        self.account_page.click_on_deposit_send()
        self.account_page.click_on_withdrawl()
        self.account_page.click_on_amount_of_withdrawl()
        self.account_page.click_on_withdrawl_send()
        self.account_page.check_balance()
        self.account_page.click_on_transcantion()
        self.transactions_page.is_opened()
        self.transactions_page.trans_to_csv()