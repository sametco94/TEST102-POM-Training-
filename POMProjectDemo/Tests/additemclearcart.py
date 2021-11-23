from selenium import webdriver
import unittest
import time
from SampleProjects.POMProjectDemo.Pages.HomePage import HomePage
from SampleProjects.POMProjectDemo.Pages.ShoppingCartPage import ShoppingCartPage


class AddItemClearCartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_additem(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(3)

        homepage = HomePage(driver)

        for k in range(3):
            homepage.add_random_product(driver)

    def test_clearcart(self):
        driver = self.driver

        homepage = HomePage(driver)
        shoppingcartpage = ShoppingCartPage(driver)

        homepage.see_shoppingcart()
        shoppingcartpage.remove_all(driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("\nTest completed!")
