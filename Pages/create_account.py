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
    phone = "phone"
    Continue_btn = "//button[@type='submit'][contains(.,'Continuar')]"



    def __init__(self, setup):
        self.driver = setup

    def session_btn(self):
        self.driver.find_element(By.XPATH, self.iniciar_sesion).click()

    def create_account(self):
        create = (By.XPATH, self.create_accnt)
        create_btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(create))
        create_btn.click()

    def username(self, email):
        user = (By.ID, self.user_field)
        user_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(user))
        user_email.send_keys(email)

    def password(self, passw):
        paswrd = (By.ID, self.psswrd_field)
        user_psswrd = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(paswrd))
        user_psswrd.send_keys(passw)

    def create_bton(self):
        btn = (By.XPATH, self.create_accnt_btn)
        b_wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(btn))
        b_wait.click()

    def form_usern(self, name):
        f_user = (By.ID, self.form_name)
        user_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(f_user))
        user_name.send_keys(name)

    def form_lname(self, name):
        f_lname = (By.ID, self.form_last_name)
        user_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(f_lname))
        user_name.send_keys(name)
