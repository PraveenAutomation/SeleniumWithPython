from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.maximize_window()
driver.get('http://www.pavantestingtools.com/')
print(driver.title)
driver.get('http://newtours.demoaut.com/')
print(driver.title)
time.sleep(5)
driver.quit()

driver.back()
print(driver.title)
time.sleep(5)

driver.forward()
print(driver.title)
time.sleep(5)