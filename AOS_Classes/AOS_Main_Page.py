from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOS_Main_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def categories_options(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".container>.rowSection>.categoryCell")

    def categories_list(self,number):
        return self.categories_options()[number-1]
    