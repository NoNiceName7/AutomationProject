from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AOS_Toolbar:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def returning_main_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".logo>a").click()

    def small_window(self):
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        small_window = self.driver.find_element(By.CSS_SELECTOR, "ul>li>#toolTipCart>div>table>tfoot>tr>td>span>label")
        total = small_window.text
        return total

    def color_check(self, number):
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        colors_texts = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label/span")
        color = colors_texts[number - 1].text
        return color

    def name_check(self, number):
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        name_texts = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/h3")
        name = name_texts[number - 1].text
        return name

    def quantity_check(self, number):
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        quantities = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label[1]")
        product_quantity = quantities[number - 1].text
        return product_quantity

    def price_check(self, number):
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        price_texts = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[3]/p")
        price = price_texts[number - 1].text
        return price

    def removing_product(self, number):
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        products = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[3]/div/div")
        remove_product = products[number - 1]
        remove_product.click()

    def edit_shopping_cart(self, number): #shoppingcartclass
        self.driver.find_element(By.ID, "shoppingCartLink").click()
        edit = self.driver.find_elements(By.CSS_SELECTOR, ".actions>a[class='edit ng-scope']")
        edit[number - 1].click()

    def quantity_check_cart_page(self,product_num): #shoppingcartclass
        product_edit = self.driver.find_elements(By.XPATH,"//table/tbody/tr/td[5]/label[2]")
        return product_edit[product_num-1].text

    def total_of_order(self):
        """This function enters the shopping cart, finds the total and returns it as a float"""
        self.driver.find_element(By.ID, "shoppingCartLink").click()
        total = self.driver.find_element(By.XPATH, "//div/section/article/div/table/tfoot/tr/td[2]/span[2]")
        total = total.text.replace("$", "").replace(",", "")
        total = float(total)
        return total



