from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class AOS_Login:

    def __init__(self, driver: webdriver.Chrome):
        """"A Constructor of the Class"""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_login_window(self):
        """This function opens the login window"""
        self.driver.find_element(By.CSS_SELECTOR, "svg[id='menuUser']").click()

    def sign_in(self, username, password):
        """This function signs into an account"""
        username_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_field.send_keys(password)
        self.driver.find_element(By.ID, "sign_in_btnundefined").click()

    def check_signed_in(self):
        """This function checks if the user is signed in """
        return self.driver.find_element(By.XPATH, "//nav/ul/li[3]/a/span").text

    def check_sign_out(self):
        """This function checks if the user is signed out """
        return self.driver.find_element(By.XPATH, "//a[@id='menuUserLink']/span")

    def sign_out(self):
        """This function signs out the user"""
        self.driver.find_element(By.CSS_SELECTOR, "svg[id='menuUser']").click()
        options = self.driver.find_elements(By.XPATH, "//li/a/div/label[@class='option roboto-medium ng-scope']")
        options[2].click()

    def login_order_payment(self, username, password):
        """"This function login at order payment page"""
        username_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='usernameInOrderPayment']")
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='passwordInOrderPayment']")
        password_field.send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[id='login_btnundefined']").click()
