from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from AOS_Classes.AOS_Main_Page import AOS_Main_Page
from AOS_Classes.AOS_Speakers_Page import AOS_Speakers_Page

# 1
service_chrome = Service(r"D:\Program Files\Expris Academy\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)
Main_page = AOS_Main_Page(driver)
Speakers_page = AOS_Speakers_Page(driver)
Main_page.categories_list(1).click()
Speakers_page.speaker_list(4).click()

sleep(10)