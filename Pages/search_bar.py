from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class search_product:

    tenis_gym_hombre = "//span[@classname='showWhiteSpace'][contains(.,'tenis gym hombre')]"
    product_displayed_options = "//li[@class='col-lg-6 col-xl col-6 pl-2 pr-2']"
    under_armor = "//span[@classname='showWhiteSpace'][contains(.,'under armor hombre')]"
    not_available = "//p[@class='a-sayt-nf-title']"
    expand_categories = "//i[@class='icon-hammenu i-hammenu']"
    hombre = "//li[@data-submenu-id='CAT5020003'][contains(.,'Hombre')]"
    tenis_de_hombre = "//a[@href='/tienda/tenis-de-hombre/catst7543627'][contains(.,'Tenis de Hombre')]"

    def __init__(self, driver):
        self.driver = driver

    def open_categories(self):
        self.driver.find_element(By.XPATH, self.expand_categories).click()

    def categories_man(self):
        man_link = self.driver.find_element(By.XPATH, self.hombre)
        actions = ActionChains(self.driver)
        actions.move_to_element(man_link).perform()

    def tenis_hombre(self):
        self.driver.find_element(By.XPATH, self.tenis_de_hombre).click()

    def brand_nike(self):
        brand_fil = (By.XPATH, self.samsung_filter)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(brand_fil))







