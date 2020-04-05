import unittest
from selenium import webdriver

class checkboxTest(unittest.TestCase):
    driver=webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')
    driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
    driver.maximize_window()
    driver.implicitly_wait(5)

    def test_singleChkbox(self):
        ele=self.driver.find_element_by_xpath("//div/label/input[@id='isAgeSelected']")
        print(ele.is_selected())
        ele1 = self.driver.find_element_by_xpath("//div/label/input[@id='isAgeSelected']").click()
        print(ele1.is_selected())
    def test_multiChkbox(self):
        self.driver.find_element_by_xpath("(//div/label/input[@class='cb1-element'])[1]").click()
        self.driver.find_element_by_xpath("(//div/label/input[@class='cb1-element'])[2]").click()

def create_suit():
    testSuit=unittest.TestSuite()
    testSuit.addTest(checkboxTest.test_singleChkbox())
    testSuit.addTest(checkboxTest.test_singleChkbox())
    return testSuit


if __name__=='__main__':
    suite=create_suit()
    runner=unittest.TextTestRunner()
    runner.run(suite)


