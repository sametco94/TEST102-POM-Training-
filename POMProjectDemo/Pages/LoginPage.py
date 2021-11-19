class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.mainpage_button_id = "header_logo"

        self.emailcreate_textbox_id = "email_create"
        self.emailcreate_button_id = "SubmitCreate"

        self.email_textbox_id = "email"
        self.password_textbox_id = "passwd"
        self.signin_button_id = "SubmitLogin"

    def goto_mainpage(self):
        self.driver.find_element_by_id(self.mainpage_button_id).click()

    def emailcreate(self, emailcreate):
        self.driver.find_element_by_id(self.emailcreate_textbox_id).send_keys(emailcreate)

    def goto_emailcreate(self):
        self.driver.find_element_by_id(self.emailcreate_button_id).click()

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def signin(self):
        self.driver.find_element_by_id(self.signin_button_id).click()
