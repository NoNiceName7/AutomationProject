from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AOS_Product_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def add_to_cart(self):
        """"Clicking on Add to Cart"""
        return self.driver.find_element(By.CSS_SELECTOR, ".fixedBtn>button").click()

    def quantity_change(self, number):
        """"Update the quantity of product"""
        quantity = self.driver.find_element(By.NAME, "quantity")
        quantity.click()
        return quantity.send_keys(number)

    def small_window(self):
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        small_window = self.driver.find_element(By.CSS_SELECTOR, "ul>li>#toolTipCart>div>table>tfoot>tr>td>span>label")
        total = small_window.text
        return total

    def get_name(self):
        """This function returns the name of the product"""
        return self.driver.find_element(By.XPATH, "//div/section/article/div/div[2]/h1").text
    def get_unit_price(self):
        """This function gets the unit price of the product and returns it as a float"""
        unit_price = self.driver.find_element(By.XPATH, "//div/section/article/div/div[2]/h2")
        unit_price = unit_price.text.replace("$", "").replace(",", "")
        unit_price = float(unit_price)
        return unit_price


# wait for the history element to be visible
# wait = WebDriverWait()
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td[class='ng-binding']")))