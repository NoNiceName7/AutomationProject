from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOS_Mice_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def mice_type(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "ul>li[class='ng-scope']>img")

    def mice_list(self, number):
        return self.mice_type()[number - 1]

    def add_to_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".fixedBtn>button").click()

    def quantity_change(self, number):
        quantity = self.driver.find_element(By.NAME, "quantity")
        quantity.click()
        return quantity.send_keys(number)