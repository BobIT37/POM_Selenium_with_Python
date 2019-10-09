from POM.POMProjectDemo.Locators.LoginPageLocator import LoginLocator
from POM.POMProjectDemo.GenericFunctions.WriteData import writeData

class LoginPage():

    #creating constructor
    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_name = LoginLocator.login_username_textbox_name
        self.password_textbox_name = LoginLocator.login_password_textbox_name
        self.login_button_name= LoginLocator.login_button_name



    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()


