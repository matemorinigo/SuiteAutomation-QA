import pytest
from selenium import webdriver
import os
from Pages import Login


class Test_Login:

    @pytest.fixture()
    def Driver(self):
        os.environ['PATH'] += r'C:\Users\Mateo\PycharmProjects\SuiteAutomation-QA\SeleniumDrivers'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        yield driver

        driver.close()
        driver.quit()

    def test_unsuccessfulLogin_033(self, Driver):
        loginPage = Login.LoginPage(Driver)
        loginPage.openLoginPage()

        loginPage.insertUsername('aaaaaaaaaaaaaaaa')
        loginPage.insertPassword('aaaaaaaaaaaaaaaa')
        loginPage.clickLoginButton()

        assert loginPage.checkErrorMessage()

    def test_successfulLogin_008(self, Driver):
        loginPage = Login.LoginPage(Driver)
        loginPage.openLoginPage()

        loginPage.insertUsername('usuario')
        loginPage.insertPassword('12345Aa!')
        loginPage.clickLoginButton()

        assert loginPage.checkSuccessfulLogin()



