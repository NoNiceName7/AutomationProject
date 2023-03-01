from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PetStore_Main_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver