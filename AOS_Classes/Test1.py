from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from AOS_Classes.AOS_Main_Page import AOS_Main_Page
from AOS_Classes.AOS_Speakers_Page import AOS_Speakers_Page
from AOS_Classes.AOS_Tablet_Page import AOS_Tablet_Page
from AOS_Classes.AOS_Headphones_Page import AOS_Headphones_Page
from AOS_Classes.AOS_Mice_Page import AOS_Mice_Page
from AOS_Classes.AOS_Toolbar import AOS_Toolbar

# 1
service_chrome = Service(r"D:\Program Files\Expris Academy\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)
Main_page = AOS_Main_Page(driver)
Return_main_page = AOS_Toolbar(driver)
# Speakers_page = AOS_Speakers_Page(driver)
Main_page.categories_list(4).click()
# Headphones_page = AOS_Headphones_Page(driver)
# Headphones_page.headphone_list(2).click()
# Tablet_page=AOS_Tablet_Page(driver)
# Speakers_page.speaker_list(4).click()
# Tablet_page.list_of_tablets(1).click()
Mice_page = AOS_Mice_Page(driver)
Mice_page.mice_list(2).click()
Mice_page.quantity_change(2)
sleep(2)
Mice_page.add_to_cart()
sleep(2)
Return_main_page.returning_main_page()
sleep(10)
