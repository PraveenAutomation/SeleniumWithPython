import time
from selenium import webdriver

driver=webdriver.Chrome('../Drivers/chromedriver.exe')
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(5)

status=driver.find_element_by_name('sex').is_selected()
print(status)
driver.find_element_by_name('sex').click()
time.sleep(5)
status=driver.find_element_by_name('sex').is_selected()
print(status)

status1=driver.find_element_by_id('profession-0').is_selected()
print(status1)
driver.find_element_by_id('profession-0').click()
driver.find_element_by_id('profession-1').click()
status1=driver.find_element_by_id('profession-0').is_selected()
print(status1)
#driver.quit()
