import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome('../Drivers/chromedriver.exe')
driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(5)

status=driver.find_element_by_xpath("//input[@value='Male' and @ name='optradio']").is_selected()
print(status)
driver.find_element_by_xpath("//input[@value='Male' and @ name='optradio']").click()
status=driver.find_element_by_xpath("//input[@value='Male' and @ name='optradio']").is_selected()
print(status)
driver.quit()
