from selenium import webdriver
from selenium.webdriver.common.by import By


class AOS_ShoppingCart_Page:
    def __init__(self, driver: webdriver.Chrome):
        """"A Constructor of the Class"""
        self.driver = driver

    def enter_shopping_cart(self):
        """This function entering shopping cart page and return text of nav line"""
        self.driver.find_element(By.ID, "shoppingCartLink").click()
        shopping_cart_nav = self.driver.find_element(By.XPATH, "//div/section/article/nav/a[2]")
        return shopping_cart_nav.text

    def edit_shopping_cart(self, number):
        """"This function click on the select product to edit it"""
        self.driver.find_element(By.ID, "shoppingCartLink").click()
        edit = self.driver.find_elements(By.CSS_SELECTOR, ".actions>a[class='edit ng-scope']")
        edit[number - 1].click()

    def quantity_check_cart_page(self, product_num):
        """"This function return the quantity of select product in shopping cart page"""
        product_edit = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[5]/label[2]")
        return product_edit[product_num - 1].text

    def total_of_order(self):
        """This function enters the shopping cart, finds the total and returns it as a float"""
        self.driver.find_element(By.ID, "shoppingCartLink").click()
        total = self.driver.find_element(By.XPATH, "//div/section/article/div/table/tfoot/tr/td[2]/span[2]")
        total = total.text.replace("$", "").replace(",", "")
        total = float(total)
        return total

    def safepay(self, username, password):
        """"This function receives Safepay user details and insert it in the field at payment"""
        username_field = self.driver.find_element(By.NAME, "safepay_username")
        username_field.click()
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.NAME, "safepay_password")
        password_field.click()
        password_field.send_keys(password)

    def mastercard(self, card_number, cvv, cardholder_name):
        """"This function enter CreditCard details of user in payment page"""
        card_number_field = self.driver.find_element(By.CSS_SELECTOR, "input[id='creditCard']")
        card_number_field.click()
        card_number_field.send_keys(card_number)
        cvv_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cvv_number']")
        cvv_field.click()
        cvv_field.send_keys(cvv)
        cardholder_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cardholder_name']")
        cardholder_name_field.click()
        cardholder_name_field.send_keys(cardholder_name)
        self.driver.find_element(By.NAME,"save_master_credit").click()
        self.driver.find_element(By.ID, 'pay_now_btn_ManualPayment').click()
