from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.get('http://demo.automationtesting.in/Windows.html')
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.title)
print(driver.current_url)

time.sleep(5)
# driver.close() # Focused only on current browser
driver.quit() # Focused on complete instance

