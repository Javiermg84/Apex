import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#this class is the parent of all pages
#it contains all the generic methods and utilities for all the pages

class BasePage:

    searchbar = "mainSearchbar"
    zoomicon = "(//i[@class='icon-zoom'])[1]"
    Url = "https://www.liverpool.com.mx/tienda/home"
    expand_categories = "//i[@class='icon-hammenu i-hammenu']"

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_text_field(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def open_web_page(self):
        pass

    def search_bar(self, product):
        locator_sbar = (By.ID,self.searchbar)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_sbar)).clear()
        self.driver.find_element(By.ID, self.searchbar).send_keys(product)

    def zoom_icon(self):
        self.driver.find_element(By.XPATH, self.zoomicon).click()
    #self.driver.WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))

    def open_categories(self):
        locator_categories = (By.XPATH, self.expand_categories)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_categories)).click()


