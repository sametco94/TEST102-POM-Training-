import time


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

        self.mainpage_button_id = "header_logo"
        self.account_button_className = "account"
        self.login_button_className = "login"
        self.logout_button_className = "logout"
        self.contact_button_id = "contact-link"
        self.bigsize_button_id = "view_full_size"
        self.addtocard_button_id = "add_to_cart"
        self.moreinfo_box_className = "rte"
        self.nextimage_button_className = "fancybox-next"
        self.previousimage_button_className = "fancybox-prev"

    def goto_mainpage(self):
        self.driver.find_element_by_id(self.mainpage_button_id).click()

    def enterto_accountpage(self):
        self.driver.find_element_by_class_name(self.account_button_className).click()

    def see_contactpage(self):
        self.driver.find_element_by_id(self.contact_button_id).click()

    def login_accountpage(self):
        self.driver.find_element_by_class_name(self.login_button_className).click()

    def log_out(self):
        self.driver.find_element_by_class_name(self.logout_button_className).click()

    def bigsize_review(self):
        self.driver.find_element_by_id(self.bigsize_button_id).click()

    def add_to_card(self):
        self.driver.find_element_by_id(self.addtocard_button_id).click()

    def preview_moreinfo(self):
        print("THE PRODUCT DETAILS:", self.driver.find_element_by_class_name(self.moreinfo_box_className))

    def next_image(self):
        self.driver.find_element_by_class_name(self.nextimage_button_className).click()

    def previous_image(self):
        self.driver.find_element_by_class_name(self.previousimage_button_className).click()

    def imagebyimage(self, driver):
        photos = driver.find_elements_by_class_name("img-responsive")
        check = len(photos) - 2
        time.sleep(1)

        self.driver.find_element_by_id(self.bigsize_button_id).click()

        for j in range(check):
            driver.find_element_by_class_name("fancybox-next").click()
            time.sleep(1)

        driver.find_element_by_class_name("fancybox-close").click()
        time.sleep(1)
