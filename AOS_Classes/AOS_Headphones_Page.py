from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOS_Headphones_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def headphone_type(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "ul>li[class='ng-scope']>img")

    def headphone_list(self,number):
        return self.headphone_type()[number-1]
