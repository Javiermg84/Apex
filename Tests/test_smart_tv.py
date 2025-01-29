import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from Pages.smart_tv import Television
from Pages.base_Page import BasePage
from Tests.conftest import setup
from Utilities.custome_logger import Log_Maker

class Test_SmartTV:

    #logger = Log_Maker.log_gen()

    def test_smart_tv(self, setup):
        self.driver = setup

        self.driver.get(BasePage.Url)
        self.driver.maximize_window()

        self.sbar = BasePage(self.driver)
        self.sbar.search_bar("smart tv")
        self.sbar.zoom_icon()

        #self.sbar.driver.execute_script("window.scrollTo(0, 900)")

        # NOTE : assert to validate that these filters are displayed
        self.smart = Television(self.driver)
        self.smart.price_mini(6000)
        self.smart.price_maxi(9000)
        self.smart.next_btn()
        self.smart.price_filter()
        #self.smart.driver.execute_script("window.scrollTo(0, 1200)")
        self.smart.tv_visible()
        self.smart.tv_brand("samsung")
        self.smart.brand_chkbx()
        self.smart.brand_filter()

        self.smart.driver.execute_script("window.scrollTo(0, 1200)")
        self.smart.size()

        self.smart.size_filter()
        results_displayed = self.driver.find_elements(By.XPATH, Television.results_tv)
        tvs_displayed = (len(results_displayed))

        texto = self.smart.driver.find_element(By.XPATH, Television.product_results).text

        if texto == f'({tvs_displayed} resultados)':
            #self.logger.info(
                #"************* The items displayed correctly match the results ***********"
            assert True
        else:
            #self.logger.info(
                #"************* The items displayed do not correctly match the results ***********"
            self.driver.save_screenshot(".\\screenshots\\results_dont_match.png")
            assert False

        #self.smart.tvprice()
        #priceone = self.smart.driver.find_element(By.XPATH, Television.tv_price).text
        #assert priceone >= "$10,00000"



        # VALIDATE ALL THE RESULTS HAVE PRICES ABOVE 10000 PESOS
        #electronics.driver.find_element(By.XPATH, "//img[@class='a-header__logo']").click()

