import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    driver = webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')
    driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    driver.maximize_window()
    #driver.close()

    def test_1stc(self):
        #self.driver.find_element(By.ID,'user-message').send_keys('VDS TECH LABS')
        self.driver.find_element_by_css_selector('#user-message').send_keys('VDS')
        self.driver.find_element_by_xpath("//button[text()='Show Message']").click()
        value=self.driver.find_element_by_id('display')
        print(value.text)
        assert 'VDS' == value.text
        print('Assertion Successful')
        #self.driver.close()

    def test_2ndtc(self):
        self.driver.find_element_by_css_selector('#sum1').send_keys('6')
        self.driver.find_element_by_css_selector('#sum2').send_keys('6')
        self.driver.find_element_by_xpath("//button[text()='Get Total']").click()
        value=self.driver.find_element(By.ID,'displayvalue')
        print(value.text)
        assert '12' == value.text
        print('Add assertion successful')
        #self.driver.close()
    def test_singleCheckbox(self):
        self.driver

def create_suit():
    testSuit=unittest.TestSuite()
    testSuit.addTest(MyTestCase.test_1stc())
    testSuit.addTest(MyTestCase.test_2ndtc())
    return testSuit



if __name__ == '__main__':
    suit=create_suit()
    runner=unittest.TextTestRunner()
    runner.run(suit)
