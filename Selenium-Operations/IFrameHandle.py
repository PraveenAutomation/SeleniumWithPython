from selenium import webdriver
import unittest


class FrameExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.driver.implicitly_wait(30)  # Introducing Implict Wait
        self.base_url = "https://the-internet.herokuapp.com/nested_frames"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_frame(self):
        driver = self.driver
        driver.get(self.base_url)
        print(driver.page_source)
        driver.switch_to.alert(driver.find_element_by_name("frame-bottom"))
        print(driver.page_source)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

