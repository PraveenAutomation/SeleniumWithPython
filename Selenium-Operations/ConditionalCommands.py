from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.get('http://newtours.demoaut.com/')

user_ele=driver.find_element_by_name('userName')
print(user_ele.is_displayed())
print(user_ele.is_enabled())
pwd_ele=driver.find_element_by_name('password')
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())
user_ele.send_keys('mercury')
pwd_ele.send_keys('mercury')
signIn_ele=driver.find_element_by_css_selector('[name$=login]')
signIn_ele.click()
time.sleep(5)

roundtrip_ele=driver.find_element_by_css_selector('[value$=roundtrip]')
oneway_ele=driver.find_element_by_css_selector('[value$=oneway]')
print('Status of roundtrip element :',roundtrip_ele.is_selected())
print('Status of onesway element :',oneway_ele.is_selected())
driver.quit()