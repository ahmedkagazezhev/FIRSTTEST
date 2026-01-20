from selenium import webdriver
from  selenium.webdriver.common.by import By
import time
from datetime import date
import csv


link = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)

button_login = browser.find_element(By.XPATH,"//button[contains(@class,'btn-primary')]").click()

time.sleep(1)

button_choice_name = browser.find_element(By.ID,'userSelect').click()

option_harry = browser.find_element(By.XPATH, "//option[text()='Harry Potter']").click()
time.sleep(1)

button_login_harry = browser.find_element(By.XPATH,'//button[contains(@class,"btn-default")]').click()
time.sleep(1)

def fibbonachi(n:int):
    a, b = 0,1
    for _ in range(n):
       a,b = b,a+b
    return a
a = date.today().day
today = date.today()
deposit_count = fibbonachi(today.day)
deposit = browser.find_element(By.XPATH,"(//button[contains(@class,'btn btn-lg tab')])[2]").click()
time.sleep(1)

deposit_amount = browser.find_element(By.XPATH,'//input[contains(@class,"form-control")]').send_keys(deposit_count)
time.sleep(1)

deposit_button_press = browser.find_element(By.XPATH,'//button[contains(@class,"btn-default")]').click()
time.sleep(1)

withdrawl = browser.find_element(By.XPATH,"(//button[contains(@class,'btn btn-lg tab')])[3]").click()
time.sleep(1)
withdrawl_amount = browser.find_element(By.XPATH,'//input[contains(@class,"form-control")]').send_keys(deposit_count)
time.sleep(1)
withdrawl_button_press = browser.find_element(By.XPATH,'//button[contains(@class,"btn-default")]').click()
time.sleep(1)

balance = browser.find_element(By.XPATH,'(//strong[contains(@class,"ng-binding")])[2]')

# нужен pytest
# if balance.text == "0":
#     print('ok')
# else:
#     print('ne ok')
transactions = browser.find_element(By.XPATH,"(//button[contains(@class,'btn btn-lg tab')])[1]").click()
time.sleep(1)

transactions_prov1 = browser.find_element(By.ID,'anchor0')
transactions_prov2 = browser.find_element(By.ID,'anchor1')
print(transactions_prov1.text)
print(transactions_prov2.text)


transactions_prov1_chek = transactions_prov1.text.replace(",","")
transactions_prov1_chek_1 = transactions_prov1_chek.split()
first_str = transactions_prov1_chek_1[1] +" " + transactions_prov1_chek_1[0]+" "+transactions_prov1_chek_1[2]+ " "+transactions_prov1_chek_1[3]
second_str = transactions_prov1_chek_1[-2]
theard_str = transactions_prov1_chek_1[-1]

transactions_prov1_chek2 = transactions_prov1.text.replace(",","")
transactions_prov1_chek_2 = transactions_prov1_chek.split()
first_str_2 = transactions_prov1_chek_2[1] +" " + transactions_prov1_chek_2[0]+" "+transactions_prov1_chek_2[2]+ " "+transactions_prov1_chek_2[3]
second_str_2 = transactions_prov1_chek_2[-2]
theard_str_2 = transactions_prov1_chek_2[-1]

arr = [[first_str,second_str,theard_str],[first_str_2,second_str_2,theard_str_2]]

# with open('report.csv','w',newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(arr)


