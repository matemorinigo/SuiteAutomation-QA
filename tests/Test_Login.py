import pytest
from selenium import webdriver
import os
from Pages import Login, Register, HomePage, Profile


class Test_Login:

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
        myProfile = Profile.MyProfile(Driver)
        myProfile.deleteProfile()
        yield
    @pytest.fixture
    def RegisterUser(self, Driver):
        registerPage = Register.RegisterPage(Driver)
        registerPage.register("CP-009","cp009","cp009@example.com","12345Aa!")
        yield

    @pytest.fixture
    def LoginUser(self,Driver):
        loginPage = Login.LoginPage(Driver)
        loginPage.login('usuario','12345Aa!')

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

    def test_loginWithDeletedAccount_009(self, Driver, RegisterUser, DeleteUser):
        loginPage = Login.LoginPage(Driver)
        loginPage.openLoginPage()

        loginPage.insertUsername('cp009')
        loginPage.insertPassword('12345Aa!')
        loginPage.clickLoginButton()

        assert loginPage.checkErrorMessage()

    def test_loginWithTwoAccounts_010(self, Driver, LoginUser):
        Driver.execute_script("window.open('');")
        Driver.switch_to.window(Driver.window_handles[-1])

        loginPage = Login.LoginPage(Driver)
        loginPage.openLoginPage()

        loginPage.insertUsername('usuario2')
        loginPage.insertPassword('12345Aa!')
        loginPage.clickLoginButton()

        loginPage.checkSuccessfulLogin()

        homePage = HomePage.HomePage(Driver)

        assert homePage.checkUsernameLoggedEqualsTo('usuario2')



