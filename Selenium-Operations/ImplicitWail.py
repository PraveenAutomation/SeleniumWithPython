from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)


driver.get('http://newtours.demoaut.com/')
driver.find_element_by_name('userName').send_keys('mercury')
driver.find_element_by_name('password').send_keys('mercury')
print(driver.title)
assert 'Welcome: Mercury Tours' in driver.title
driver.find_element_by_css_selector('[value$=Login]').click()

driver.quit()