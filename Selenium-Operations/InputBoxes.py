import time
from selenium import webdriver

driver=webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')
driver.get('http://newtours.demoaut.com/')
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(5)

# Verify Home Page title:
print(driver.title)
assert 'Welcome: Mercury Tours' in driver.title
# Filling Registration Form
driver.find_element_by_link_text('REGISTER').click()
driver.find_element_by_name('firstName').send_keys('abc')
driver.find_element_by_name('lastName').send_keys('xyz')
time.sleep(5)
driver.find_element_by_name('phone').send_keys('78451258')
driver.find_element_by_name('register').click()

driver.quit()
