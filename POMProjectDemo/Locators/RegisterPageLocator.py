class RegisterLocator:

    # Register page locators
    # Register link
    Regiser_link_xpath = "//a[text()='REGISTER']"

    # contact_information
    firstname_textbox_name = "firstName"
    lastname_textbox_name = "lastName"
    phone_number_textbox_name = "phone"
    email_textbox_name = "userName"

    # mailing_information
    address_textbox_name = "address1"
    city_textbox_name = "city"
    state_textbox_name = "state"
    postal_code_textbox_name = "postalCode"
    country_dropdown_name = "country"

    # user_information
    register_username_textbox_name = "email"
    register_password_textbox_name = "password"
    conf_password_textbox_name = "confirmPassword"

    # Clickregister_button
    register_button_name = "register"
    registered_user_name = "//b[contains(text(),' Note: Your user name is')]"