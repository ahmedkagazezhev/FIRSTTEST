from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.fibonachi_cal_page import Fib
from datetime import date
import allure
class Account(BasePage):
    #все нужные хендлеры
    PAGE_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    DEPOSIT = ('xpath',"//button[contains(@class, 'tab') and contains(normalize-space(), 'Deposit')]")
    DEPOSIT_AMOUNT_BUTTON = ('xpath', "//input[@class='form-control ng-pristine ng-untouched ng-invalid ng-invalid-required']")
    DEPOSIT_BUTTON_SEND = ('xpath',"//button[@class='btn btn-default']")

    WITHDRAWL = ('xpath',"//button[contains(@class, 'tab') and contains(normalize-space(), 'Withdrawl')]")
    WITHDRAWL_AMOUNT_BUTTON = ('xpath',"//input[@class='form-control ng-pristine ng-untouched ng-invalid ng-invalid-required']")
    WITHDRAWL_BUTTON_SEND = ('xpath',"//button[@class='btn btn-default']")

    TRANSCANTION_BUTTON = ('xpath',"//button[contains(@class, 'tab') and contains(normalize-space(), 'Transactions')]")

    BALANCE = ('xpath',"(//strong[@class='ng-binding'])[2]")

    #кликает на кнопку депозита (одна из 3 )
    @allure.step('Click on deposit on page')
    def click_on_deposit(self):
        self.wait.until(EC.element_to_be_clickable(self.DEPOSIT)).click()


    #в amount закидывает число фибоначи сегоднящнего числа
    @allure.step('Click on amount deposit on page')
    def click_on_amount_of_deposit(self):
        self.wait.until(EC.element_to_be_clickable(self.DEPOSIT_AMOUNT_BUTTON)).send_keys(Fib.fib(date.today().day))

    #кликает на кнопку депозит после внесения числа
    @allure.step('Click on deposit send on page')
    def click_on_deposit_send(self):
        self.wait.until(EC.element_to_be_clickable(self.DEPOSIT_BUTTON_SEND)).click()

    #кликает на кнопку withdrawl (одна из 3)
    @allure.step('Click on withdrawl on page')
    def click_on_withdrawl(self):
        self.wait.until(EC.element_to_be_clickable(self.WITHDRAWL)).click()

    #в amount закидывает число фибоначи сегоднящнего числа
    @allure.step('Click on amount withdrawl on page')
    def click_on_amount_of_withdrawl(self):
        self.wait.until(EC.element_to_be_clickable(self.WITHDRAWL_AMOUNT_BUTTON)).send_keys(Fib.fib(date.today().day))

    # кликает на кнопку withdrawl после внесения числа
    @allure.step('Click on withdrawl send on page')
    def click_on_withdrawl_send(self):
        self.wait.until(EC.element_to_be_clickable(self.WITHDRAWL_BUTTON_SEND)).click()

    #кликает на транзакции и дальше перебрасывыет на другой урл
    @allure.step('Click on transcantion on page')
    def click_on_transcantion(self):
        self.wait.until(EC.element_to_be_clickable(self.TRANSCANTION_BUTTON)).click()

    #проверка баланса после внесения депозита и вычита withdrawl
    @allure.step('Check balance')
    def check_balance(self):
        a = self.wait.until(EC.element_to_be_clickable(self.BALANCE))
        assert a.text == "0", "Balance not zero"


