from selenium.webdriver.common.by import By


class Registration:
    def __init__(self, driver):
        self.driver = driver

    registerLink = (By.XPATH, "//a[normalize-space()='Register']")
    rbMale = (By.XPATH, "//input[@id='gender-male']")
    rbFemale = (By.XPATH, "//input[@id='gender-female']")
    firstName = (By.XPATH, "//input[@id='FirstName']")
    lastName = (By.XPATH, "//input[@id='LastName']")
    email = (By.XPATH, "//input[@id='Email']")
    password = (By.XPATH, "//input[@id='Password']")
    confirmPassword = (By.XPATH, "//input[@id='ConfirmPassword']")
    registerBtn = (By.XPATH, "//input[@id='register-button']")

    def clickOnRegisterLink(self):
        return self.driver.find_element(*Registration.registerLink).click()

    def clickOnMaleRadioButton(self):
        return self.driver.find_element(*Registration.rbMale).click()

    def clickOnFemaleRadioButton(self):
        return self.driver.find_element(*Registration.rbFemale).click()

    def inputFirstName(self, fname):
        return self.driver.find_element(*Registration.firstName).send_keys(fname)

    def inputLastName(self, lname):
        return self.driver.find_element(*Registration.lastName).send_keys(lname)

    def inputEmail(self, mail):
        return self.driver.find_element(*Registration.email).send_keys(mail)

    def inputPassword(self, password):
        return self.driver.find_element(*Registration.password).sendKeys(password)

    def inputConfirmPassword(self, confirm):
        return self.driver.find_element(*Registration.confirmPassword).sendKeys(confirm)

    def clickOnRegisterButton(self):
        return self.driver.find_element(*Registration.registerBtn)
