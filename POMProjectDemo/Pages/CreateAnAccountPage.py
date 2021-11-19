class CreateAnAccountPage:

    def __init__(self, driver):
        self.driver = driver

        self.gendermale_check_id = "uniform-id_gender1"
        self.genderfemale_check_id = "uniform-id_gender2"

        self.firstname_textbox_id = "customer_firstname"
        self.lastname_textbox_id = "customer_lastname"
        self.newpass_textbox_id = "passwd"
        self.days_dropdown_id = "days"
        self.months_dropdown_id = "months"
        self.years_dropdown_id = "years"
        self.newsletter_check_id = "uniform-newsletter"
        self.specials_check_id = "uniform-optin"
        self.newcompany_textbox_id = "company"
        self.newaddress1_textbox_id = "address1"
        self.newaddress2_textbox_id = "address2"
        self.newcity_texbox_id = "city"
        self.newstate_dropdown_id = "id_state"
        self.newpost_textbox_id = "postcode"
        self.newcountry_dropdown_id = "id_country"
        self.newaddition_textbox_id = "other"
        self.newhomephone_textbox_id = "phone"
        self.newmobilephone_textbox_id = "phone_mobile"
        self.newalias_textbox_id = "alias"

        self.submit_signin_button_id = "submitAccount"

        self.shopchart_button_className = "shopping_cart"

    def check_gendermale(self):
        self.driver.find_element_by_id(self.gendermale_check_id).click()

    def check_genderfemale(self):
        self.driver.find_element_by_id(self.genderfemale_check_id).click()

    def check_subscriptions(self):
        self.driver.find_element_by_id(self.newsletter_check_id).click()
        self.driver.find_element_by_id(self.specials_check_id).click()

    def filltheinfo(self, firstname, lastname, newpass, day, month, year, company, address1, address2, city, state, postcode, country, addinfo, homephone, mobilephone, alias):
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(firstname)
        self.driver.find_element_by_id(self.lastname_textbox_id).send_keys(lastname)
        self.driver.find_element_by_id(self.newpass_textbox_id).send_keys(newpass)
        self.driver.find_element_by_id(self.days_dropdown_id).send_keys(day)
        self.driver.find_element_by_id(self.months_dropdown_id).send_keys(month)
        self.driver.find_element_by_id(self.years_dropdown_id).send_keys(year)
        self.driver.find_element_by_id(self.newcompany_textbox_id).send_keys(company)
        self.driver.find_element_by_id(self.newaddress1_textbox_id).send_keys(address1)
        self.driver.find_element_by_id(self.newaddress2_textbox_id).send_keys(address2)
        self.driver.find_element_by_id(self.newcity_texbox_id).send_keys(city)
        self.driver.find_element_by_id(self.newstate_dropdown_id).send_keys(state)
        self.driver.find_element_by_id(self.newpost_textbox_id).send_keys(postcode)
        self.driver.find_element_by_id(self.newcountry_dropdown_id).send_keys(country)
        self.driver.find_element_by_id(self.newaddition_textbox_id).send_keys(addinfo)
        self.driver.find_element_by_id(self.newhomephone_textbox_id).send_keys(homephone)
        self.driver.find_element_by_id(self.newmobilephone_textbox_id).send_keys(mobilephone)
        self.driver.find_element_by_id(self.newalias_textbox_id).clear()
        self.driver.find_element_by_id(self.newalias_textbox_id).send_keys(alias)

    def submit_info(self):
        self.driver.find_element_by_id(self.submit_signin_button_id).click()