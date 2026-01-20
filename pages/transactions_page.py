from pages.base_page import BasePage
from pages.last_csv import LastCsv
import csv
import allure

class Transaction(BasePage):

    PAGE_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    FIRST_TRANS = ('id','anchor0')
    SECOND_TRANS = ('id','anchor1')

    @allure.step('Let is convert our data to CSV')
    def trans_to_csv(self):
        self.driver.refresh()
        first_trans = self.driver.find_element('id','anchor0')
        second_trans = self.driver.find_element('id','anchor1')
        a = LastCsv.lastcsv(first_trans.text,second_trans.text)
        with open('lastcsv','w',newline="") as f:
            writer = csv.writer(f)
            writer.writerows(a)
