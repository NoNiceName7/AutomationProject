from selenium import webdriver
from selenium.webdriver.common.by import By


class AOS_Main_Page:
    def __init__(self, driver: webdriver.Chrome):
        """"A Constructor of the Class"""
        self.driver = driver

    def categories_options(self):
        """"This function return list of the Categories """
        return self.driver.find_elements(By.CSS_SELECTOR, ".container>.rowSection>.categoryCell")

    def categories_list(self, number):
        """"This function return the select Category from the list"""
        return self.categories_options()[number - 1]
