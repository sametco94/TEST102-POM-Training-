class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.account_button_className = "header_user_info"
        self.contact_button_id = "contact-link"

    def enterto_accountpage(self):
        self.driver.find_element_by_class_name(self.account_button_className).click()

    def see_contactpage(self, contact):
        self.driver.find_element_by_id(self.contact_button_id).click()