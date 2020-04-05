import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://www.expedia.com/')
driver.find_element(By.ID,'tab-flight-tab-hp').click()
time.sleep(5)
driver.find_element(By.ID,'flight-origin-hp-flight').send_keys('SFO')
time.sleep(5)
driver.find_element(By.ID,'flight-destination-hp-flight').send_keys('NYC')
time.sleep(5)
driver.find_element(By.ID,'flight-departing-hp-flight').clear()
driver.find_element(By.ID,'flight-departing-hp-flight').send_keys('03/30/2020')
driver.find_element(By.ID,'flight-returning-hp-flight').clear()
driver.find_element(By.ID,'flight-returning-hp-flight').send_keys('03/31/2020')
driver.find_element(By.XPATH,'//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button').click()

# Explicit wait
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.ID,'stopFilter_stops-0')))

element.click()
time.sleep(5)
driver.quit()
#driver.find_element(By.ID,'stopFilter_stops-0').click()