from selenium import webdriver
import unittest
from POM.POMProjectDemo.GenericFunctions import ReadData
from POM.POMProjectDemo.Pages.RegisterPage import RegisterPage
import HtmlTestRunner

class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://newtours.demoaut.com/")

    def test_register(self):
        driver = self.driver
        register = RegisterPage(driver)
        register.click_register()
        register.set_contact_information(ReadData.getData("FirstName"), ReadData.getData("LastName"), ReadData.getData("Phone"), ReadData.getData("Email"))
        register.set_mailing_information(ReadData.getData("Address"), ReadData.getData("City"), ReadData.getData("State"), ReadData.getData("PostalCode"), ReadData.getData("Country"))
        register.set_user_information(ReadData.getData("Username"), ReadData.getData("Password"), ReadData.getData("Password"))
        register.click_submitregister()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\POM\\POMProjectDemo\\reports'))