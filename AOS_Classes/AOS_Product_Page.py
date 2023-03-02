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

