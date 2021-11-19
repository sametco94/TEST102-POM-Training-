class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver

        self.orderhistory_button_className = "icon-list-ol"
        self.creditslips_button_className = "icon-ban-circle"
        self.addresses_button_className = "icon-building"
        self.userinfo_button_className = "icon-user"
        self.wishlist_button_className = "icon-heart"
        self.backhome_button_className = "icon-chevron-left"
        self.account_button_className = "header_user_info"
        self.contact_button_id = "contact-link"
        self.logout_button_className = "logout"
        self.shopchart_button_className = "shopping_cart"

    def goto_orderhistory(self):
        self.driver.find_element_by_class_name(self.orderhistory_button_className).click()

    def goto_creditslist(self):
        self.driver.find_element_by_class_name(self.creditslips_button_className).click()

    def goto_addresses(self):
        self.driver.find_element_by_class_name(self.addresses_button_className).click()

    def goto_presonalinfo(self):
        self.driver.find_element_by_class_name(self.userinfo_button_className).click()

    def goto_wishlist(self):
        self.driver.find_element_by_class_name(self.wishlist_button_className).click()

    def goto_backhome(self):
        self.driver.find_element_by_class_name(self.backhome_button_className).click()

    def goto_logout(self):
        self.driver.find_element_by_class_name(self.logout_button_className).click()

    def goto_shopcart(self):
        self.driver.find_element_by_class_name(self.shopchart_button_className).click()