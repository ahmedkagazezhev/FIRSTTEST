import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CustomerLoginPage(BasePage):
    PAGE_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    YOUR_NAME = ('xpath','//option[text()="Harry Potter"]')
    Customer_Login_Page = ('xpath','//button[text()="Login"]')

    #выбирает потера и логинется
    @allure.step('Choice name')
    def choice_name(self):
        self.wait.until(EC.element_to_be_clickable(self.YOUR_NAME)).click()

    @allure.step('Click on login in customer page')
    def login_customer_page(self):
        self.wait.until(EC.element_to_be_clickable(self.Customer_Login_Page)).click()

