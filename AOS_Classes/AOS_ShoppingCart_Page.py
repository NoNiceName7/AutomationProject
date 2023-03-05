from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AOS_ShoppingCart_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def enter_shopping_cart(self):
        self.driver.find_element(By.ID, "shoppingCartLink").click()
        shopping_cart_nav = self.driver.find_element(By.XPATH, "//div/section/article/nav/a[2]")
        return shopping_cart_nav.text

    def edit_shopping_cart(self, number):
        self.driver.find_element(By.ID, "shoppingCartLink").click()
        edit = self.driver.find_elements(By.CSS_SELECTOR, ".actions>a[class='edit ng-scope']")
        edit[number - 1].click()

    def quantity_check_cart_page(self, product_num):
        product_edit = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[5]/label[2]")
        return product_edit[product_num - 1].text

    def total_of_order(self):
        """This function enters the shopping cart, finds the total and returns it as a float"""
        self.driver.find_element(By.ID, "shoppingCartLink").click()
        total = self.driver.find_element(By.XPATH, "//div/section/article/div/table/tfoot/tr/td[2]/span[2]")
        total = total.text.replace("$", "").replace(",", "")
        total = float(total)
        return total
