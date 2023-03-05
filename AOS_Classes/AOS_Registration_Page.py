from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AOS_Registration_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def create_account(self, username, password, email):
        """Creating New Account"""
        username_field = self.driver.find_element(By.NAME, "usernameRegisterPage")
        username_field.click()
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.NAME, "passwordRegisterPage")
        password_field.click()
        password_field.send_keys(password)
        confirm_field = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
        confirm_field.click()
        confirm_field.send_keys(password)
        email_field = self.driver.find_element(By.NAME, "emailRegisterPage")
        email_field.click()
        email_field.send_keys(email)
