import pytest

from Utilities.BaseClass import BaseClass
from pageObjects.LogInPage import LoginPage
from pageObjects.RegistrationPage import Registration


class Test01(BaseClass):

    def test_registerUser(self):
        register = Registration(self.driver)
        register.clickOnRegisterLink()
        register.clickOnMaleRadioButton()
        register.inputFirstName("Lucky")
        register.inputLastName("paul")
        register.inputEmail("lucky123@gmail.com")
        register.inputPassword("Lucky@123")
        register.inputConfirmPassword("Lucky@123")
        register.clickOnRegisterButton()

    def loginFunctionality(self):
        login = LoginPage(self.driver)
        login.clickOnLoginLink()
        login.inputUsername("Lucky")
        login.inputPassword("1234")
        login.clickOnLoginBtn()
