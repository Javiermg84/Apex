from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Television:
    #Locators
    # self.expand_categories = (By.XPATH,"//i[@class='icon-hammenu i-hammenu']")
    # self.hovere = (By.XPATH,"//a[@href='/tienda/electrónica/cat5150041']")
    # self.click_tv = (By.XPATH,"(//a[@href='/tienda/pantallas/catst14457077'])[1]")
    tv_brand_search = "//input[@id='searchBrand']"
    #price_range = "//div[@class='m-radioButton mdc-form-field'][contains(.,'$5000.0 -$10000.0')]"
    Brand_checkbox = "//input[@id='brand-SAMSUNG'][@type='checkbox']"
    samsung_filter = "//div[@class='newChipContainer'][contains(.,'SAMSUNG')]"
    inches = "//input[@id='variants.normalizedSize-50 pulgadas']"
    OLEDTech = "//input[@id='dynamicFacets.pantallaatt-OLED']"
    product_results = "//span[@class='searchNum-result']"
    filter_div = "//div[@class='m-plp__filterSection '][20]"
    tv_descr = "//h3[@class='card-title a-card-description'][contains(.,'Pantalla Smart TV Sony LCD de 55 pulgadas 4K KD-55X77L')]"
    tv_image = "//img[@id='img_0']"
    tv_price = "(//p[@class='a-card-discount'])[1]"
    results_tv = "//li[@class='m-product__card card-masonry a']"
    filter_size_tv = "//div[@class='newChipContainer'][contains(.,'50 pulgadas')]"
    price_min = "min-price-filter"
    price_max = "max-price-filter"
    next_bttn = "//span[@class='next-button__filter']"
    filter_price_range = "//div[@class='newChipContainer'][contains(.,'$6000.0 -$9000.0')]"

    # init and locators
    def __init__(self, driver):
        self.driver = driver

    #Actions
    def explicit_wait(self, locator):
        self.driver.WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))

    def tv_brand(self, brand):
        locator_brand = (By.XPATH, self.tv_brand_search)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_brand)).send_keys(brand)

    def texto(self):
        texto = self.driver.find_element(By.XPATH, self.product_results).text

    def tvprice(self):
        price =  self.driver.find_element(By.XPATH, self.tv_price).text
        print(price)

    def tv_results_displayed(self):
        results_displayed = self.driver.find_element(By.XPATH, self.results_tv)

    #def do_send_keys(self, by_locator, text):
    #    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(find_element(locator_brand))).send_keys(brand)

    def brand_chkbx(self):
        self.driver.find_element(By.XPATH,self.Brand_checkbox).click()

    def size(self):
        self.driver.find_element(By.XPATH,self.inches).click()

    def brand_visible_filter(self):
        brand_filter_vis = (By.XPATH, self.product_results)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(brand_filter_vis))

    def brand_filter(self):
        brand_fil = (By.XPATH, self.samsung_filter)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(brand_fil))

    def tv_visible(self):
        tv_visi = (By.XPATH,self.tv_image)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(tv_visi))

    def size_filter(self):
        filter_visible = (By.XPATH, self.filter_size_tv)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(filter_visible))

    def price_filter(self):
        price_fil = (By.XPATH, self.filter_price_range)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(price_fil))

    def results(self):
        count = (By.XPATH,self.product_results)
        count_results = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(count)).text
        print(count_results)

    def move_to_element(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.filter_div)
        actions.move_to_element(element)

    def price_mini(self, minim):
        self.driver.find_element(By.ID, self.price_min).send_keys(minim)

    def price_maxi(self, maxim):
        self.driver.find_element(By.ID, self.price_max).send_keys(maxim)

    def next_btn(self):
        self.driver.find_element(By.XPATH, self.next_bttn).click()


