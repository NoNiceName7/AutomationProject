from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from AOS_Classes.AOS_Main_Page import AOS_Main_Page
from AOS_Classes.AOS_Category_Page import AOS_Category_Page
from AOS_Classes.AOS_Toolbar import AOS_Toolbar
from AOS_Classes.AOS_Product_Page import AOS_Product_Page


class TestAOS_Main_Page(TestCase):
    def setUp(self):
        service_chrome = Service(r"D:\Program Files\Expris Academy\Selenium\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.Main_page = AOS_Main_Page(self.driver)
        self.Return_main_page = AOS_Toolbar(self.driver)

    def test_checking_cart_items(self):
        """Checking when adding 2 different products with different quantity
        showing the correct details at cart window"""
        self.Main_page.categories_list(4).click()
        mice_page = AOS_Category_Page(self.driver)
        mice_page.product_list(2).click()
        mice_product = AOS_Product_Page(self.driver)
        mice_product.quantity_change(2)
        sleep(2)
        mice_product.add_to_cart()
        sleep(2)
        self.Return_main_page.returning_main_page()
        self.Main_page.categories_list(1).click()
        speaker_page = AOS_Category_Page(self.driver)
        speaker_page.product_list(3).click()
        speaker_page = AOS_Product_Page(self.driver)
        speaker_page.quantity_change(4)
        sleep(2)
        speaker_page.add_to_cart()
        sleep(2)
        self.Return_main_page.returning_main_page()
        sleep(10)

