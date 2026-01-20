import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


#начальная первая страница
class LoginPage(BasePage):

    PAGE_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    CUSTOMER_LOGIN = ('xpath',"//button[contains(@class,'btn-primary')]")

    #заход в кастомер логин
    @allure.step('Click on Customer login')
    def login_customer(self):
        self.wait.until(EC.element_to_be_clickable(self.CUSTOMER_LOGIN)).click()