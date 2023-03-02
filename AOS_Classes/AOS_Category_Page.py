from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOS_Category_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def product_type(self):
        """"Finding elements of different products"""
        return self.driver.find_elements(By.CSS_SELECTOR, "ul>li[class='ng-scope']>img")

    def product_list(self, number):
        """"Returning element of the select product"""
        return self.product_type()[number - 1]


