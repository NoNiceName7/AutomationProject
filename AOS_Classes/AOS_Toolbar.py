from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AOS_Toolbar:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def returning_main_page(self):
        self.driver.find_element(By.CSS_SELECTOR,".logo>a").click()

    def small_window(self):
        """"Checking the total quantity at the window cart """
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        small_window = self.driver.find_element(By.CSS_SELECTOR, "ul>li>#toolTipCart>div>table>tfoot>tr>td>span>label")
        total = small_window.text
        return total

    def color_check(self,number):
        """"Selected the wanted color text of product"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        colors_texts = self.driver.find_elements(By.XPATH,"//table/tbody/tr/td[2]/a/label/span")
        color = colors_texts[number-1].text
        return color

    def name_check(self,number):
        """"Selected the wanted name text of product"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        name_texts = self.driver.find_elements(By.XPATH,"//table/tbody/tr/td[2]/a/h3")
        name = name_texts[number-1].text
        return name

    def quantity_check(self, number):
        """"Selected the wanted quantity text of product"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        quantities = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label[1]")
        product_quantity = quantities[number - 1].text
        return product_quantity

    def price_check(self,number):
        """"Selected the wanted price text of product without $ """
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        price_texts = self.driver.find_elements(By.XPATH,"//table/tbody/tr/td[3]/p")
        price = price_texts[number-1].text
        return price[1:]

