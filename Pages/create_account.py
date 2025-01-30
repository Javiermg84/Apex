from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class New_Account:

    iniciar_sesion = "//span[@class='a-header__topLink'][contains(.,'Iniciar sesión')]"
    create_accnt = "//a[@class='c9b47022f cd0498a37'][contains(.,'Crear cuenta')]"
    user_field = "email"
    psswrd_field = "password"
    create_accnt_btn = "//button[@type='submit'][contains(.,'Crear cuenta')]"
    form_name = "input-user__name"
    form_last_name = "input-user__apaterno"
    day = "daySelectorLabel"
    month = "monthSelectorLabel"
    year = "yearSelectorLabel"
    sexo = "male"
    create_accnt_btn_two = "//button[@class='a-btn a-btn--primary']"
    phone = "//input[@class='input c20b8ca2a cb0163f2a'][@id='phone']"
    Continue_btn = "//button[@type='submit'][contains(.,'Continuar')]"
    country_drpdwn = "//button[@value='pick-country-code']"
    country_search = "//input[@class='input cdf05dcc8__search-input']"
    choose_c = "//button[@aria-label='Estados Unidos (+1)'][@value='selection-action::US1']"



    def __init__(self, setup):
        self.driver = setup

    def session_btn(self):
        self.driver.find_element(By.XPATH, self.iniciar_sesion).click()

    def create_account(self):
        create = (By.XPATH, self.create_accnt)
        create_btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(create))
        create_btn.click()

    def wrong_email(self, wrongemail):
        self.driver.find_element(By.ID, self.user_field).send_keys(wrongemail)

    def form_date(self, one_number, letter_e):
        self.driver.find_element(By.ID, self.day).send_keys(one_number)
        self.driver.find_element(By.ID, self.month).send_keys(letter_e)
        self.driver.find_element(By.ID, self.year).send_keys(one_number)

    def gender(self):
        self.driver.find_element(By.ID, self.sexo).click()

    def create_btn_two(self):
        self.driver.find_element(By.XPATH, self.create_accnt_btn_two).click()

    def username_clear(self):
        user = (By.ID, self.user_field)
        user_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(user))
        user_email.clear()

    def username(self, email):
        user = (By.ID, self.user_field)
        user_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(user))
        user_email.send_keys(email)

    def password(self, passw):
        paswrd = (By.ID, self.psswrd_field)
        user_psswrd = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(paswrd))
        user_psswrd.send_keys(passw)

    def password_clear(self, passw):
        paswrd = (By.ID, self.psswrd_field)
        user_psswrd = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(paswrd))
        user_psswrd.clear()

    def create_bton(self):
        btn = (By.XPATH, self.create_accnt_btn)
        b_wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(btn))
        b_wait.click()

    def form_usern(self, usern):
        f_user = (By.ID, self.form_name)
        user_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(f_user))
        user_name.send_keys(usern)

    def form_lname(self, last_name):
        f_lname = (By.ID, self.form_last_name)
        user_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(f_lname))
        user_name.send_keys(last_name)

    def phone_num(self, p_num):
        p_locator = (By.XPATH, self.phone)
        phone_number = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(p_locator))
        phone_number.send_keys(p_num)

    def continue_btn(self):
        self.driver.find_element(By.XPATH, self.Continue_btn).click()

    def country(self):
        c_drpdwn = (By.XPATH, self.country_drpdwn)
        country = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(c_drpdwn))
        country.click()

    def country_search_field(self, country):
        c_field = (By.XPATH, self.country_search)
        c_search = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(c_field))
        c_search.send_keys(country)

    def country_field_clear(self):
        c_field = (By.XPATH, self.country_search)
        c_search = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(c_field))
        c_search.clear()

    def choose_usa(self):
        c_usa = (By.XPATH, self.choose_c)
        chooseusa = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(c_usa))
        chooseusa.click()



