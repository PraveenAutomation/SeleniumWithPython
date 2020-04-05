from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(5)

# Find how many input boxes in a Web Page:
inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))

# Verify the status of Input Boxes:
st1=driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
dst2=driver.find_element(By.ID,'RESULT_TextField-2').is_displayed()
print('Enabled Status = ',st1,', ' 'Display Status = ',dst2)

# How to input value in input boxes:
driver.find_element_by_id('RESULT_TextField-1').send_keys('VDS')
driver.find_element_by_id('RESULT_TextField-2').send_keys('TECH')
driver.find_element_by_id('RESULT_TextField-3').send_keys(45896552368)

driver.quit()