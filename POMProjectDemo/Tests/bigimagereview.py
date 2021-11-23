from selenium import webdriver
import unittest
import time
from SampleProjects.POMProjectDemo.Pages.HomePage import HomePage
from SampleProjects.POMProjectDemo.Pages.ProductPage import ProductPage


class BigImageReviewTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_bigimagereview(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(3)

        homepage = HomePage(driver)
        productpage = ProductPage(driver)

        for i in range(3):
            homepage.see_random_product(driver)
            time.sleep(1)
            productpage.imagebyimage(driver)
            productpage.goto_mainpage()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed!")
