class MyAddressesPage:

    def __init__(self, driver):
        self.driver = driver

        self.addressupdate_button_xPath = "//*[@id='center_column']/div[1]/div/div/ul/li[9]/a[1]"
        self.removeupdate_button_className = "icon-remove"
        self.addnewaddress_button_linkText = "address"
        self.backtoaccount_button_linkText = "my-account"
        self.backtohome_button_link = "http://automationpractice.com"

    def addressupdate(self):
        self.driver.find_element_by_xpath(self.addressupdate_button_xPath).click()
    def addressdelete(self):
        self.driver.find_element_by_class_name(self.removeupdate_button_className).click()
    def newaddressadd(self):
        self.driver.find_element_by_partial_link(self.addnewaddress_button_linkText).click()
    def backtoaccount(self):
        self.driver.find_element_by_partial_link(self.backtoaccount_button_linkText).click()
    def backtohome(self):
        self.driver.find_element_by_link(self.backtohome_button_link).click()