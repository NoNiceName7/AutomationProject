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
        self.toolbar = AOS_Toolbar(self.driver)

    def test_checking_cart_items(self):
        """Checking when adding 2 different products with different quantity
        showing the correct total at cart window"""
        self.Main_page.categories_list(4).click()
        mice_page = AOS_Category_Page(self.driver)
        mice_page.product_list(2).click()
        mice_product = AOS_Product_Page(self.driver)
        mice_product.quantity_change(2)
        mice_product.add_to_cart()
        self.toolbar.returning_main_page()
        self.Main_page.categories_list(1).click()
        speaker_page = AOS_Category_Page(self.driver)
        speaker_page.product_list(3).click()
        speaker_product = AOS_Product_Page(self.driver)
        speaker_product.quantity_change(4)
        speaker_product.add_to_cart()
        self.toolbar.returning_main_page()
        total = AOS_Toolbar(self.driver).small_window()
        self.assertIn('6', total)
        self.toolbar.returning_main_page()

    def test_correct_products(self):
        """"Checking if the product name,quantity,color,price are correct"""
        # add a speaker
        self.Main_page.categories_list(1).click()
        speaker_page = AOS_Category_Page(self.driver)
        speaker_page.product_list(2).click()
        speaker_product = AOS_Product_Page(self.driver)
        speaker_product.quantity_change(2)
        speaker_product.add_to_cart()
        self.toolbar.returning_main_page()
        # add a tablet
        self.Main_page.categories_list(2).click()
        tablet_page = AOS_Category_Page(self.driver)
        tablet_page.product_list(3).click()
        tablet_product = AOS_Product_Page(self.driver)
        tablet_product.quantity_change(3)
        tablet_product.add_to_cart()
        self.toolbar.returning_main_page()
        # add a laptop
        self.Main_page.categories_list(3).click()
        laptop_page = AOS_Category_Page(self.driver)
        laptop_page.product_list(4).click()
        laptop_product = AOS_Product_Page(self.driver)
        laptop_product.quantity_change(4)
        laptop_product.add_to_cart()
        self.toolbar.returning_main_page()
        # check the quantity of the products in the cart
        speaker_q = AOS_Toolbar(self.driver).quantity_check(3)
        self.assertIn('2', speaker_q)
        tablet_q = AOS_Toolbar(self.driver).quantity_check(2)
        self.assertIn('3', tablet_q)
        laptop_q = AOS_Toolbar(self.driver).quantity_check(1)
        self.assertIn('4', laptop_q)
        # check the color of the products in the cart
        speaker_c = AOS_Toolbar(self.driver).color_check(3)
        self.assertEqual('TURQUOISE', speaker_c)
        tablet_c = AOS_Toolbar(self.driver).color_check(2)
        self.assertEqual('BLACK', tablet_c)
        laptop_c = AOS_Toolbar(self.driver).color_check(1)
        self.assertEqual('GRAY', laptop_c)
        # check the name of the products in the cart
        speaker_name = AOS_Toolbar(self.driver).name_check(3)
        self.assertEqual('BOSE SOUNDLINK WIRELESS SPE...', speaker_name)
        tablet_name = AOS_Toolbar(self.driver).name_check(2)
        self.assertEqual('HP PRO TABLET 608 G1', tablet_name)
        laptop_name = AOS_Toolbar(self.driver).name_check(1)
        self.assertEqual('HP ENVY X360 - 15T LAPTOP', laptop_name)
        # check the price of the products
        speaker_price = AOS_Toolbar(self.driver).price_check(3)
        self.assertEqual('$258.00', speaker_price)
        tablet_price = AOS_Toolbar(self.driver).price_check(2)
        self.assertEqual('$1,437.00', tablet_price)
        laptop_price = AOS_Toolbar(self.driver).price_check(1)
        self.assertEqual('$2,799.96', laptop_price)
        self.toolbar.returning_main_page()

    def test_remove_product(self):
        """"Removing product from cart window and checking if total is correct"""
        # add a headphone
        self.Main_page.categories_list(5).click()
        headphone_page = AOS_Category_Page(self.driver)
        headphone_page.product_list(1).click()
        headphone_product = AOS_Product_Page(self.driver)
        headphone_product.add_to_cart()
        self.toolbar.returning_main_page()
        # add a laptop
        self.Main_page.categories_list(3).click()
        laptop_page = AOS_Category_Page(self.driver)
        laptop_page.product_list(11).click()
        laptop_product = AOS_Product_Page(self.driver)
        laptop_product.add_to_cart()
        self.toolbar.returning_main_page()
        # removing headphone product
        product = AOS_Toolbar(self.driver)
        product.removing_product(2)
        total = AOS_Toolbar(self.driver).small_window()
        self.assertIn('1', total)
        self.toolbar.returning_main_page()

    def test_cart_page_nav(self):
        # add a laptop
        self.Main_page.categories_list(3).click()
        laptop_page = AOS_Category_Page(self.driver)
        laptop_page.product_list(10).click()
        laptop_product = AOS_Product_Page(self.driver)
        laptop_product.add_to_cart()
        cart_nav = AOS_Toolbar(self.driver).enter_shopping_cart()
        self.assertEqual("SHOPPING CART", cart_nav)
        self.toolbar.returning_main_page()
    def test_correct_total(self):
        """This test checks that the sum of the totals for each product ordered is the same as the total in the cart"""
        # Order the speakers and print the description of the order
        self.Main_page.categories_list(1).click()
        speaker_page = AOS_Category_Page(self.driver)
        speaker_page.product_list(6).click()
        speaker_product = AOS_Product_Page(self.driver)
        speaker = AOS_Product_Page(self.driver)
        speaker_n = speaker.get_name()
        speaker_p = speaker.get_unit_price()
        speaker_number = 2
        speaker_q = speaker.quantity_change(speaker_number)
        speaker.add_to_cart()
        print(f"product name = {speaker_n}\nproduct price = {speaker_p}\nproduct quantity = {speaker_number}")
        self.toolbar.returning_main_page()
        # Order the tablets and print the description of the order
        self.Main_page.categories_list(2).click()
        tablet_page = AOS_Category_Page(self.driver)
        tablet_page.product_list(1).click()
        tablet = AOS_Product_Page(self.driver)
        tablet_n = tablet.get_name()
        tablet_p = tablet.get_unit_price()
        tablet_number = 3
        tablet_q = tablet.quantity_change(tablet_number)
        print(f"product name = {tablet_n}\nproduct price = {tablet_p}\nproduct quantity = {tablet_number}")
        tablet.add_to_cart()
        self.toolbar.returning_main_page()
        # Order the laptops and print the description of the order
        self.Main_page.categories_list(3).click()
        laptop_page = AOS_Category_Page(self.driver)
        laptop_page.product_list(1).click()
        laptop = AOS_Product_Page(self.driver)
        laptop_n = laptop.get_name()
        laptop_p = laptop.get_unit_price()
        laptop_number = 4
        laptop_q = laptop.quantity_change(laptop_number)
        laptop.add_to_cart()
        print(f"product name = {laptop_n}\nproduct price = {laptop_p}\nproduct quantity = {laptop_number}")
        # Calculate the amount the order is supposed to be
        total_speaker = speaker_p * speaker_number
        total_tablet = tablet_p * tablet_number
        total_laptop = laptop_p * laptop_number
        total_purchase = total_laptop + total_tablet + total_speaker
        # get the amount of the total in the shopping cart and compare with the previous calculation
        total_shopping_cart = AOS_Toolbar(self.driver)
        total_in_sc = total_shopping_cart.total_of_order()
        self.assertEqual(total_purchase, total_in_sc)
        self.toolbar.returning_main_page()

    def test_edit_quantity_in_cart(self):
        # add a laptop
        self.Main_page.categories_list(3).click()
        laptop_page = AOS_Category_Page(self.driver)
        laptop_page.product_list(9).click()
        laptop_product = AOS_Product_Page(self.driver)
        laptop_product.add_to_cart()
        self.toolbar.returning_main_page()
        # add a headphone
        self.Main_page.categories_list(5).click()
        headphone_page = AOS_Category_Page(self.driver)
        headphone_page.product_list(4).click()
        headphone_product = AOS_Product_Page(self.driver)
        headphone_product.add_to_cart()
        self.toolbar.returning_main_page()
        edit = AOS_Toolbar(self.driver)
        # press the button 'edit' in shopping cart page
        edit.edit_shopping_cart(2)
        laptop_product.quantity_change(2)
        laptop_product.add_to_cart()
        sleep(5)
        quantity1 = AOS_Toolbar(self.driver).quantity_check_cart_page(2)
        self.assertEqual("2",quantity1)  # bug
        edit.edit_shopping_cart(1)
        headphone_product.quantity_change(3)
        headphone_product.add_to_cart()
        quantity2 = AOS_Toolbar(self.driver).quantity_check_cart_page(1)
        sleep(5)
        self.assertEqual("3",quantity2)
        self.toolbar.returning_main_page()







