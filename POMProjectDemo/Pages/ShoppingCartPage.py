import time


class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver

        self.mainpage_button_id = "header_logo"
        self.addone_button_className = "icon-plus"
        self.removeone_button_className = "icon-minus"
        self.mainpage_button_id = "header_logo"

    def goto_mainpage(self):
        self.driver.find_element_by_id(self.mainpage_button_id).click()

    def add_one_more(self):
        self.driver.find_element_by_class_name(self.addone_button_className).click()

    def remove_one(self):
        self.driver.find_element_by_class_name(self.removeone_button_className).click()

    def remove_all(self, driver):
        clear_elem = driver.find_elements_by_class_name("clear_cart")
        check = len(clear_elem)
        items = driver.find_elements_by_class_name("icon-trash")
        remover = len(items)
        if check <= 0:
            print("\nClear Cart option does not exist!")
            for i in range(remover):
                driver.find_element_by_class_name("icon-trash").click()
                time.sleep(2)
            print("Shopping cart is successfully cleared")
            self.driver.find_element_by_id(self.mainpage_button_id).click()
        else:
            driver.clear_elem.click()
            print("Shopping cart is successfully cleared")
            self.driver.find_element_by_id(self.mainpage_button_id).click()
        time.sleep(2)