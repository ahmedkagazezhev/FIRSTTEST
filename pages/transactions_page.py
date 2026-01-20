from pages.base_page import BasePage
from pages.last_csv import LastCsv
import csv
import allure

class Transaction(BasePage):

    PAGE_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    FIRST_TRANS = ('id','anchor0')
    SECOND_TRANS = ('id','anchor1')

    #перезагружаю страницу тк иногда не появляются транзы и нужно перегзагрзить
    #беру две транзы и фарширую в нужный формат пункта 10 в 20 строчке

    @allure.step('Let is convert our data to CSV')
    def trans_to_csv(self):
        self.driver.refresh()
        first_trans = self.driver.find_element('id','anchor0')
        second_trans = self.driver.find_element('id','anchor1')
        a = LastCsv.lastcsv(first_trans.text,second_trans.text)
        with open('lastcsv','w',newline="") as f:
            writer = csv.writer(f)
            writer.writerows(a)
