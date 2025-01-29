import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from Pages.search_bar import search_product
from Pages.smart_tv import Television
from Pages.base_Page import BasePage
from Tests.conftest import setup
from Utilities.custome_logger import Log_Maker

class Test_SearchBar:

    #logger = Log_Maker.log_gen()

    def test_product(self, setup):
        self.driver = setup

        self.driver.get(BasePage.Url)
        self.driver.maximize_window()

        self.sbar = BasePage(self.driver)
        self.sbar.search_bar("tenis gym")
        #self.sbar.zoom_icon()

        #at least one option for "tenis gym" should be displayed as suggestion
        self.product = search_product(self.driver)
        product_tenis_one = self.product.driver.find_element(By.XPATH, search_product.tenis_gym_hombre)
        tenis_text = product_tenis_one.text
        assert "tenis gym" in tenis_text

        #assert > products related are displayed correctly

        options_displayed = self.driver.find_elements(By.XPATH, search_product.product_displayed_options)
        tenis_displayed = (len(options_displayed))

        if tenis_displayed >= 1 :
            #self.logger.info("************* The search is successfully displaying suggestions for the client ***********")
            assert True
        else:
            #self.logger.info("************* There are no suggestions for the product searched ***********")
            self.driver.save_screenshot(".\\screenshots\\no_suggestions_displayed.png")
            assert False

    '''***************************************************************************************'''

    #Test Case 2
    #user is writing a brand, incorrectly. The search bar should display the correct option and suggest products.
    def test_wrong_brand(self, setup):
        self.driver = setup

        self.driver.get(BasePage.Url)
        self.driver.maximize_window()

        self.sbar = BasePage(self.driver)
        self.sbar.search_bar("onder almor") #Under Armor

        """ at least one option for "under armor" should be displayed as suggestion """
        self.product = search_product(self.driver)
        under_armor_brand = self.product.driver.find_element(By.XPATH, search_product.under_armor)
        ua_text = under_armor_brand.text

        assert "under armor" in ua_text

        """ assert > products related are displayed correctly"""
        options_brand = self.driver.find_elements(By.XPATH, search_product.product_displayed_options)
        options_displayed = (len(options_brand))

        if options_displayed >= 1:
            # self.logger.info("************* The search is successfully displaying suggestions for the client ***********")
            assert True
        else:
            # self.logger.info("************* There are no suggestions for the product searched ***********")
            self.driver.save_screenshot(".\\screenshots\\no_options_displayed.png")
            assert False

    '''***************************************************************************************'''

    """ Test Case 1.2.01 User write a model of a product that is not available"""
    def test_model(self, setup):
        self.driver = setup

        self.driver.get(BasePage.Url)
        self.driver.maximize_window()

        self.sbar = BasePage(self.driver)
        self.sbar.search_bar("ADhydj84659XF")

        """ assert > "No encontramos resultados" is in the text displayed in the search """
        self.product = search_product(self.driver)
        model = self.product.driver.find_element(By.XPATH, search_product.not_available)
        model_text = model.text

        assert "No encontramos resultados" in model_text

    '''***************************************************************************************'''

    """  TC 1.2.02 User write a brand of a product that is not available  """
    """  brand > Yoplait  ,  expected > "No encontramos resultados" """

    def test_brand_unavailable(self, setup):
        self.driver = setup

        self.driver.get(BasePage.Url)
        self.driver.maximize_window()

        self.sbar = BasePage(self.driver)
        self.sbar.search_bar("Yoplait")

        """ assert > "No encontramos resultados" is in the text displayed in the search """
        self.product = search_product(self.driver)
        brand = self.product.driver.find_element(By.XPATH, search_product.not_available)
        brand_text = brand.text

        assert "No encontramos resultados" in brand_text

'''***************************************************************************************'''

    """   TC 1.3.01 Search an article by brand, physical characteristic, model  """
    """  Categorias > Hombre > Tenis de hombre > Nike > 27.5 > Negro  """
    """  assert > comparacion resultados con mostrados  """

    def test_nike(self, setup):
        self.driver = setup










