from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class search_product:

    tenis_gym_hombre = "//span[@classname='showWhiteSpace'][contains(.,'tenis gym hombre')]"
    product_displayed_options = "//li[@class='col-lg-6 col-xl col-6 pl-2 pr-2']"
    under_armor = "//span[@classname='showWhiteSpace'][contains(.,'under armor hombre')]"
    not_available = "//p[@class='a-sayt-nf-title']"

    def __init__(self, driver):
        self.driver = driver



