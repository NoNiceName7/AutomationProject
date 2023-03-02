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
        self.driver.find_element(By.CSS_SELECTOR,".logo>a").click()

    def small_window(self):
        shopping_cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(shopping_cart_icon).perform()
        small_window = self.driver.find_element(By.CSS_SELECTOR, "ul>li>#toolTipCart>div>table>tfoot>tr>td>span>label")
        total = small_window.text
        return total