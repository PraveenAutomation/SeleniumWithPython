import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')

driver.get('http://newtours.demoaut.com/')
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(5)

# No. of links in Demo site:
links=driver.find_elements(By.TAG_NAME,'a')
print('No. of links in demo site: ',len(links))
# Name of Total links:
print('Total links:')
for link in links:
    print(link.text)

# Click on link based on "Link test" and 'Partial link text'
#driver.find_element(By.LINK_TEXT,'Cruises').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'REG').click()
time.sleep(5)
#driver.quit()