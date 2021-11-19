class UpdateAddressPage:

    def __init__(self, driver):
        self.driver = driver

        self.firstname_textbox_id = "firstname"
        self.lastname_textbox_id = "lastname"
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

        self.submit_newaddress_button_id = "submitAddress"

        self.backtoaddresses_button_xPath = "//*[@id='center_column']/ul/li/a"

    def updateaddress(self, firstname, lastname, company, address1, address2, city, state, postcode, country, addinfo, homephone, mobilephone, alias):
        self.driver.find_element_by_id(self.firstname_textbox_id).clear()
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(firstname)
        self.driver.find_element_by_id(self.lastname_textbox_id).clear()
        self.driver.find_element_by_id(self.lastname_textbox_id).send_keys(lastname)
        self.driver.find_element_by_id(self.newcompany_textbox_id).clear()
        self.driver.find_element_by_id(self.newcompany_textbox_id).send_keys(company)
        self.driver.find_element_by_id(self.newaddress1_textbox_id).clear()
        self.driver.find_element_by_id(self.newaddress1_textbox_id).send_keys(address1)
        self.driver.find_element_by_id(self.newaddress2_textbox_id).clear()
        self.driver.find_element_by_id(self.newaddress2_textbox_id).send_keys(address2)
        self.driver.find_element_by_id(self.newcity_texbox_id).clear()
        self.driver.find_element_by_id(self.newcity_texbox_id).send_keys(city)
        self.driver.find_element_by_id(self.newstate_dropdown_id).send_keys(state)
        self.driver.find_element_by_id(self.newpost_textbox_id).clear()
        self.driver.find_element_by_id(self.newpost_textbox_id).send_keys(postcode)
        self.driver.find_element_by_id(self.newcountry_dropdown_id).send_keys(country)
        self.driver.find_element_by_id(self.newaddition_textbox_id).clear()
        self.driver.find_element_by_id(self.newaddition_textbox_id).send_keys(addinfo)
        self.driver.find_element_by_id(self.newhomephone_textbox_id).clear()
        self.driver.find_element_by_id(self.newhomephone_textbox_id).send_keys(homephone)
        self.driver.find_element_by_id(self.newmobilephone_textbox_id).clear()
        self.driver.find_element_by_id(self.newmobilephone_textbox_id).send_keys(mobilephone)
        self.driver.find_element_by_id(self.newalias_textbox_id).clear()
        self.driver.find_element_by_id(self.newalias_textbox_id).send_keys(alias)

    def saveupdatedaddress(self):
        self.driver.find_element_by_id(self.submit_newaddress_button_id).click()

    def backtoaddresses(self):
        self.driver.find_element_by_xpath(self.backtoaddresses_button_xPath).click()
