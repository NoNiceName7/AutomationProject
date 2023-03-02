from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from AOS_Classes.AOS_Main_Page import AOS_Main_Page
from AOS_Classes.AOS_Category_Page import AOS_Category_Page
from AOS_Classes.AOS_Toolbar import AOS_Toolbar
from AOS_Classes.AOS_Product_Page import AOS_Product_Page

# 1
service_chrome = Service(r"D:\Program Files\Expris Academy\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)
Main_page = AOS_Main_Page(driver)
Return_main_page = AOS_Toolbar(driver)
# Speakers_page = AOS_Speakers_Page(driver)
Main_page.categories_list(4).click()
# Headphones_page = AOS_Headphones_Page(driver)
# Headphones_page.headphone_list(2).click()
# Tablet_page=AOS_Tablet_Page(driver)
# Speakers_page.speaker_list(4).click()
# Tablet_page.list_of_tablets(1).click()
Mice_page = AOS_Category_Page(driver)
Mice_page.product_list(2).click()
Mice_product= AOS_Product_Page(driver)
Mice_product.quantity_change(2)
sleep(2)
Mice_product.add_to_cart()
sleep(2)
Return_main_page.returning_main_page()
sleep(10)


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
    self.assertEqual("2", quantity1)  # bug
    edit.edit_shopping_cart(1)
    headphone_product.quantity_change(3)
    headphone_product.add_to_cart()
    quantity2 = AOS_Toolbar(self.driver).quantity_check_cart_page(1)
    sleep(5)
    self.assertEqual("3", quantity2)
    self.toolbar.returning_main_page()

    def edit_shopping_cart(self, number): #shoppingcartclass
        self.driver.find_element(By.ID, "shoppingCartLink").click()
        edit = self.driver.find_elements(By.CSS_SELECTOR, ".actions>a[class='edit ng-scope']")
        edit[number - 1].click()

    def quantity_check_cart_page(self,product_num): #shoppingcartclass
        product_edit = self.driver.find_elements(By.XPATH,"//table/tbody/tr/td[5]/label[2]")
        return product_edit[product_num-1].text
