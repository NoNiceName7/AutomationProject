from selenium import webdriver
from selenium.webdriver.common.by import By


class AOS_Category_Page:
    def __init__(self, driver: webdriver.Chrome):
        """"A Constructor of the Class"""
        self.driver = driver

    def product_type(self):
        """"Finding elements of different products"""
        return self.driver.find_elements(By.CSS_SELECTOR, "ul>li[class='ng-scope']>img")

    def product_list(self, number):
        """"Returning element of the select product"""
        return self.product_type()[number - 1]
