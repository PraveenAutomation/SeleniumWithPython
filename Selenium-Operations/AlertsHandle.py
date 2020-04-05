import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)
popAlert=driver.switch_to.alert
time.sleep(5)
#popAlert.accept()
popAlert.dismiss()
