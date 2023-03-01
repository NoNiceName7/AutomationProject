from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tablets_Page:

    def __init__(self, driver:webdriver.chrome):
        self.driver = driver

    def tablet_options(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "ul>li[class='ng-scope']>img")

    def list_of_tablets(self, number):
        return self.tablet_options()[number-1]
