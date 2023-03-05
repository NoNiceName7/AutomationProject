from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class AOS_Toolbar:
    def __init__(self, driver: webdriver.Chrome):
        """"A Constructor of the Class"""
        self.driver = driver

    def returning_main_page(self):
        """"This function return to the Main page of site by clicking logo """
        self.driver.find_element(By.CSS_SELECTOR, ".logo>a").click()

    def small_window(self):
        """"This function checks the total quantity at cart window"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        small_window = self.driver.find_element(By.CSS_SELECTOR, "ul>li>#toolTipCart>div>table>tfoot>tr>td>span>label")
        total = small_window.text
        return total

    def color_check(self, number):
        """"This function returns the select color text"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        colors_texts = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label/span")
        color = colors_texts[number - 1].text
        return color

    def name_check(self, number):
        """"This function returns the select name text"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        name_texts = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/h3")
        name = name_texts[number - 1].text
        return name

    def quantity_check(self, number):
        """"This function returns the select quantity text"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        quantities = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label[1]")
        product_quantity = quantities[number - 1].text
        return product_quantity

    def price_check(self, number):
        """"This function returns the select price text"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        price_texts = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[3]/p")
        price = price_texts[number - 1].text
        return price

    def removing_product(self, number):
        """This function removes a product from shopping cart window"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        products = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[3]/div/div")
        remove_product = products[number - 1]
        remove_product.click()

    def checkout(self):
        """"This function clicks on checkout button"""
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        self.driver.find_element(By.XPATH, "//table/tfoot/tr[2]/td/button").click()


