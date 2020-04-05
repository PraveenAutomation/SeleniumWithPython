import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(5)

element=driver.find_element(By.ID,'RESULT_RadioButton-9')
#  Select dropdown by using Select class:
drpList=Select(element)

# Count the no. of drop down options:
print('No of drop down lists: ',len(drpList.options))
all_option=drpList.options
for option in all_option:
    print(option.text)

# Print all optins in drop down :

# By Using 'visible text'
# drpList.select_by_visible_text('Morning')
# # By Using 'INDEX'
drpList.select_by_index(2)
time.sleep(10)
# By Using 'VALUE'
#drpList.select_by_value('Radio-1')

driver.quit()
