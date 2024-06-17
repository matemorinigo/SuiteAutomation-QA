import pytest
from selenium import webdriver
import os
from Pages import Register, Profile


class Test_Register:

    @pytest.fixture
    def Driver(self):
        os.environ['PATH'] += r'C:\Users\Mateo\PycharmProjects\SuiteAutomation-QA\SeleniumDrivers'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        yield driver

        driver.close()
        driver.quit()

    @pytest.fixture
    def DeleteUser(self, Driver):
        yield
        myProfile = Profile.MyProfile(Driver)
        myProfile.deleteProfile()

    @pytest.fixture
    def RegisterUser(self, Driver):
        registerPage = Register.RegisterPage(Driver)
        registerPage.register("CP-005","cp005","cp005@example.com","12345Aa!")
        yield


    def test_successfulRegister_001(self, DeleteUser, Driver):
        registerPage = Register.RegisterPage(Driver)
        registerPage.openRegisterPage()

        registerPage.insertName('NombreTest')
        registerPage.insertUsername('UserTest')
        registerPage.insertEmail('EmailTest@example.com')

        registerPage.insertPassword('12345Aa!')
        registerPage.confirmPassword('12345Aa!')

        registerPage.clickRegisterButton()

        assert registerPage.checkSuccessfulRegister()

    def test_invalidEmail_002(self, Driver):
        registerPage = Register.RegisterPage(Driver)
        registerPage.openRegisterPage()

        registerPage.insertName('NombreTest')
        registerPage.insertUsername('UserTest')
        registerPage.insertEmail('invalidEmail')

        registerPage.insertPassword('12345Aa!')
        registerPage.confirmPassword('12345Aa!')

        registerPage.clickRegisterButton()

        assert registerPage.checkErrorMessageEmail()

    def test_invalidPassword_003(self, Driver):
        registerPage = Register.RegisterPage(Driver)
        registerPage.openRegisterPage()

        registerPage.insertName('NombreTest')
        registerPage.insertUsername('UserTest')
        registerPage.insertEmail('invalidEmail')

        registerPage.insertPassword('12345678')
        registerPage.confirmPassword('12345678')

        registerPage.clickRegisterButton()

        assert registerPage.checkErrorMessageInvalidPassword()

    def test_passwordDoesntMatch_004(self, Driver):
        registerPage = Register.RegisterPage(Driver)
        registerPage.openRegisterPage()

        registerPage.insertName('NombreTest')
        registerPage.insertUsername('UserTest')
        registerPage.insertEmail('email@example.com')

        registerPage.insertPassword('12345Aa!')
        registerPage.confirmPassword('12345Ab!')

        registerPage.clickRegisterButton()

        assert registerPage.checkErrorMessagePasswordMustMatch()

    def test_userAlreadyExists_005(self, Driver, RegisterUser):
        registerPage = Register.RegisterPage(Driver)
        registerPage.openRegisterPage()

        registerPage.insertName('NombreTest')
        registerPage.insertUsername('cp005')
        registerPage.insertEmail('notUsedEmail@example.com')

        registerPage.insertPassword('12345Aa!')
        registerPage.confirmPassword('12345Aa!')

        registerPage.clickRegisterButton()

        assert registerPage.checkErrorMessagePasswordMustMatch()