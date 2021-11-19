class PersonalInfoPage:

    def __init__(self, driver):
        self.driver = driver

        self.gendermale_check_id = "uniform-id_gender1"
        self.genderfemale_check_id = "uniform-id_gender2"

        self.firstname_textbox_id = "firstname"
        self.lastname_textbox_id = "lastname"
        self.email_textbox_id = "email"
        self.days_dropdown_id = "days"
        self.months_dropdown_id = "months"
        self.years_dropdown_id = "years"
        self.oldpass_textbox_id = "old_passwd"
        self.newpass_textbox_id = "passwd"
        self.confirmation_textbox_id = "confirmation"
        self.newsletter_check_id = "uniform-newsletter"
        self.specials_check_id = "uniform-optin"

        self.backtoaccount_button_xPath = "//*[@id='center_column']/ul/li[1]/a/span/i"
        self.backtohome_button_link = "http://automationpractice.com"
        self.save_button_xPath = "//*[@id='center_column']/div/form/fieldset/div[11]/button/span"

    def check_gendermale(self):
        self.driver.find_element_by_id(self.gendermale_check_id).click()

    def check_genderfemale(self):
        self.driver.find_element_by_id(self.genderfemale_check_id).click()

    def check_subscriptions(self):
        self.driver.find_element_by_id(self.newsletter_check_id).click()
        self.driver.find_element_by_id(self.specials_check_id).click()

    def editinfo(self, firstname, lastname, email, day, month, year, oldpass, newpass, confirmation):
        self.driver.find_element_by_id(self.firstname_textbox_id).clear()
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(firstname)
        self.driver.find_element_by_id(self.lastname_textbox_id).clear()
        self.driver.find_element_by_id(self.lastname_textbox_id).send_keys(lastname)
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)
        self.driver.find_element_by_id(self.oldpass_textbox_id).send_keys(oldpass)
        self.driver.find_element_by_id(self.newpass_textbox_id).send_keys(newpass)
        self.driver.find_element_by_id(self.confirmation_textbox_id).send_keys(confirmation)
        self.driver.find_element_by_id(self.days_dropdown_id).send_keys(day)
        self.driver.find_element_by_id(self.months_dropdown_id).send_keys(month)
        self.driver.find_element_by_id(self.years_dropdown_id).send_keys(year)

    def saveinfo(self):
        self.driver.find_element_by_xpath(self.save_button_xPath).click()

    def backtoaccount(self):
        self.driver.find_element_by_xpath(self.backtoaccount_button_xPath).click()

    def backtohome(self):
        self.driver.find_element_by_link(self.backtohome_button_link).click()