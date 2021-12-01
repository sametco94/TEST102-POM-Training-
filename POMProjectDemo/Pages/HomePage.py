import time
import random


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.account_button_className = "header_user_info"
        self.contact_button_id = "contact-link"
        self.shoppingcart_button_className = "shopping_cart"

    def enterto_accountpage(self):
        self.driver.find_element_by_class_name(self.account_button_className).click()

    def see_contactpage(self):
        self.driver.find_element_by_id(self.contact_button_id).click()

    def see_shoppingcart(self):
        self.driver.find_element_by_class_name(self.shoppingcart_button_className).click()
        time.sleep(2)

    def see_random_product(self, driver):
        elems = driver.find_elements_by_class_name("product_img_link")
        products = []
        for item in elems:
            a = item.get_attribute("href")
            products.append(a)
        driver.get(random.choice(products))
        time.sleep(1)

    def add_random_product(self, driver):
        elems = driver.find_elements_by_class_name("ajax_add_to_cart_button")
        products = []
        for item in elems:
            a = item.get_attribute("href")
            products.append(a)
        driver.get(random.choice(products))
        time.sleep(1)
        driver.find_element_by_id("header_logo").click()
        time.sleep(1)