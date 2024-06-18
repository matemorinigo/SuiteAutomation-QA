from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages import HomePage as HP

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.usernameInput = (By.CSS_SELECTOR, 'input[type="text"][aria-label="Username"]')
        self.passwordInput = (By.CSS_SELECTOR, 'input[type="password"][aria-label="Password"]')

        self.loginButton = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.registerButton = (By.XPATH, '//*[@id="root"]/div/div/div/button')

        self.loginPageText = (By.XPATH, '//h1[text()="Enter your email or @username"]')

        self.errorMessage = (By.XPATH, '//*[@id="root"]/div/div/div/form/label[1]')
        self.loginPageURL = r'https://frontend-training-taupe.vercel.app/login'

    def openLoginPage(self):
        self.driver.get(self.loginPageURL)

    def insertUsername(self, username):
        self.driver.find_element(*self.usernameInput).send_keys(username)

    def insertPassword(self, password):
        self.driver.find_element(*self.passwordInput).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(*self.loginButton).click()

    def checkErrorMessage(self):
        try:
            WebDriverWait(self.driver,60).until(
                EC.presence_of_element_located(self.errorMessage)
            )
            return True
        except:
            return False

    def checkSuccessfulLogin(self):
        homePage = HP.HomePage(self.driver)
        return homePage.checkHomePageLoaded()

    def login(self, username, password):
        homePage = HP.HomePage(self.driver)
        self.openLoginPage()
        self.insertUsername(username)
        self.insertPassword(password)
        self.clickLoginButton()

        homePage.checkHomePageLoaded()


    def checkLoginPageLoaded(self):
        try:
            WebDriverWait(self.driver,30).until(
                EC.presence_of_element_located(self.loginPageText)
            )
            return True
        except:
            return False








