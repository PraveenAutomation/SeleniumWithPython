from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
# driver=webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')
# driver=webdriver.Ie(executable_path='../Drivers/IEDriverServer.exe')
driver.get('http://newtours.demoaut.com/')
print(driver.current_url)
# print(driver.page_source)

print(driver.title)
driver.close()
driver.quit()