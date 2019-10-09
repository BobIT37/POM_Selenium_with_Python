from selenium import webdriver
import unittest
from POM.POMProjectDemo.GenericFunctions import ReadData
from POM.POMProjectDemo.Pages.loginPage import LoginPage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://newtours.demoaut.com/")

    def test_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username(ReadData.getData("UserID"))
        login.enter_password(ReadData.getData("PWD"))
        login.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\POM\\POMProjectDemo\\reports'))
