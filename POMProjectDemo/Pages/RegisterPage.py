from selenium.webdriver.support.ui import Select
from POM.POMProjectDemo.Locators.RegisterPageLocator import RegisterLocator
from POM.POMProjectDemo.GenericFunctions.WriteData import writeData

class RegisterPage():

    # creating constructor
    def __init__(self, driver):
        self.driver = driver

        #Register link
        self.Regiser_link_xpath = RegisterLocator.Regiser_link_xpath

        #contact_information
        self.firstname_textbox_name = RegisterLocator.firstname_textbox_name
        self.lastname_textbox_name = RegisterLocator.lastname_textbox_name
        self.phone_number_textbox_name = RegisterLocator.phone_number_textbox_name
        self.email_textbox_name = RegisterLocator.email_textbox_name

        #mailing_information
        self.address_textbox_name = RegisterLocator.address_textbox_name
        self.city_textbox_name = RegisterLocator.city_textbox_name
        self.state_textbox_name = RegisterLocator.state_textbox_name
        self.postal_code_textbox_name = RegisterLocator.postal_code_textbox_name
        self.country_dropdown_name = RegisterLocator.country_dropdown_name

        #user_information
        self.username_textbox_name = RegisterLocator.register_username_textbox_name
        self.password_textbox_name = RegisterLocator.register_password_textbox_name
        self.conf_password_textbox_name = RegisterLocator.conf_password_textbox_name

        #Clickregister_button
        self.register_button_name = RegisterLocator.register_button_name
        self.user_name = RegisterLocator.registered_user_name

    def click_register(self):
        self.driver.find_element_by_xpath(self.Regiser_link_xpath).click()

    def set_contact_information(self, firstname, lastname, phonenumber, emailaddress):
        rTitle = self.driver.title
        writeData.writeRTitle(rTitle)
        self.driver.find_element_by_name(self.firstname_textbox_name).send_keys(firstname)
        self.driver.find_element_by_name(self.lastname_textbox_name).send_keys(lastname)
        self.driver.find_element_by_name(self.phone_number_textbox_name).send_keys(phonenumber)
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(emailaddress)

    def set_mailing_information(self, addressdetial, cityname, statename, postal, countryname):
        self.driver.find_element_by_name(self.address_textbox_name).send_keys(addressdetial)
        self.driver.find_element_by_name(self.city_textbox_name).send_keys(cityname)
        self.driver.find_element_by_name(self.state_textbox_name).send_keys(statename)
        self.driver.find_element_by_name(self.postal_code_textbox_name).send_keys(postal)
        select = Select(self.driver.find_element_by_name(self.country_dropdown_name))
        select.select_by_visible_text(countryname)

    def set_user_information(self, username, password, cnfpassword):
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)
        self.driver.find_element_by_name(self.conf_password_textbox_name).send_keys(cnfpassword)

    def click_submitregister(self):
        self.driver.find_element_by_name(self.register_button_name).click()
        userName = self.driver.find_element_by_xpath(self.user_name).text
        userName = userName.split('Note: Your user name is ')[1]
        writeData.writeUser(userName)