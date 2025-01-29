import time
import random
import pytest
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
    usern = random.choice(nombres)
    email = f"{usern}{numeros}@{usern}{numeros}.com"


    def test_create_account(self, setup):
        self.driver = setup

        self.driver.get(BasePage.Url)
        self.driver.maximize_window()

        self.accnt = New_Account(self.driver)
        self.accnt.session_btn()
        self.accnt.create_account()
        self.accnt.username(self.email)
        self.accnt.password("TestApex#11")
        self.accnt.driver.execute_script("window.scrollTo(0, 200)")
        self.accnt.create_bton()
        time.sleep(20)

