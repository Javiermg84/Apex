import time
import random
import pytest
from pytest_html.extras import FORMAT_TEXT
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from Pages.smart_tv import Television
from Pages.base_Page import BasePage
from Tests.conftest import setup
from Utilities.custome_logger import Log_Maker
from Pages.create_account import New_Account


class Test_Account:

    numeros = random.randrange(1,999999)
    nombres = ["javi","erik","francia","richard","mary","jason","zeke","derek","john","jose","luis"]
    apellidos = ["rodriguez", "molina", "lopez", "suarez", "arreola", "perez", "gonzalez"]
    usern = random.choice(nombres)
    email = f"{usern}{numeros}@{usern}{numeros}.com"
    last_name = random.choice(apellidos)
    invalid_email = "//span[@class='ulp-input-error-message'][contains(.,'El correo electrónico no es válido.')]"
    p_num = random.randrange(0,11)
    no_country = "//div[@id='with-search-alert']"


    def test_create_account(self, setup):
        self.driver = setup

        self.driver.get(BasePage.Url)
        self.driver.maximize_window()

        """  TC 3.1.01 Consumer is able to create an account  """
        """  Positive and Negative tests + assertions  """

        self.accnt = New_Account(self.driver)
        self.accnt.session_btn()
        self.accnt.create_account()
        self.accnt.wrong_email("sfgsdg")
        self.accnt.password("TestApex#11")
        self.accnt.driver.execute_script("window.scrollTo(0, 200)")
        self.accnt.create_bton()
        warning = self.driver.find_element(By.XPATH, self.invalid_email)
        warning_text = warning.text

        """  Assert for warning message  """
        if "El correo electrónico no es válido." in warning_text:
            #log
            assert True
        else:
            #log
            #screenshot
            assert False

        self.accnt.username_clear()
        self.accnt.username(self.email)
        self.accnt.password("TestApex#11")
        self.accnt.driver.execute_script("window.scrollTo(0, 200)")
        self.accnt.create_bton()

        """ Filling the registration form """

        self.accnt.form_usern(self.usern)
        self.accnt.form_lname(self.last_name)
        self.accnt.form_date(1,"e")
        self.accnt.gender()
        self.accnt.create_btn_two()

        """  Testing the country dropdown  """

        self.accnt.country()
        self.accnt.country_search_field("fgjgfjfj")
        warning_no_c = self.driver.find_element(By.XPATH, self.no_country)
        warn_no_c = warning_no_c.text

        if "No se han encontrado resultados" in warn_no_c:
            #log
            assert True
        else:
            #log
            #screenshot
            assert False

        self.accnt.country_field_clear()
        self.accnt.country_search_field("Estados Unidos")
        self.accnt.choose_usa()

        """ country and phone """

        self.accnt.phone_num(self.p_num)
        self.accnt.continue_btn()


        time.sleep(50)

