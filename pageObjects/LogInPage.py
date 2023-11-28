from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    loginLink = (By.XPATH, "//a[normalize-space()='Log in']")
    username = (By.XPATH, "//input[@id='Email']")
    password = (By.XPATH, "//input[@id='Password']")
    remember = (By.XPATH, "//input[@id='RememberMe']")
    forgot = (By.XPATH, "//a[normalize-space()='Forgot password?']")
    loginBtn = (By.XPATH, "//input[@value='Log in']")

    def clickOnLoginLink(self):
        return self.driver.find_element(*LoginPage.loginLink).click()

    def inputUsername(self, name):
        return self.driver.find_element(*LoginPage.username).send_keys(name)

    def inputPassword(self, password):
        return self.driver.find_element(*LoginPage.password).send_keys(password)

    def clickOnRememberMe(self):
        return self.driver.find_element(*LoginPage.remember).click()

    def clickOnForgotBtn(self):
        return self.driver.find_element(*LoginPage.forgot).click()

    def clickOnLoginBtn(self):
        return self.driver.find_element(*LoginPage.loginBtn).click()