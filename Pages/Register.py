from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages import HomePage as HP

class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

        self.nameInput = (By.CSS_SELECTOR, 'input[type="text"][aria-label="Name"]')
        self.usernameInput = (By.CSS_SELECTOR, 'input[type="text"][aria-label="Username"]')
        self.emailInput = (By.CSS_SELECTOR, 'input[type="text"][aria-label="Email"]')
        self.passwordInput = (By.CSS_SELECTOR, 'input[type="password"][aria-label="Password"]')
        self.confirmPasswordInput = (By.CSS_SELECTOR, 'input[type="password"][aria-label="Confirm Password"]')

        self.registerButton = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.loginButton = (By.XPATH, '//*[@id="root"]/div/div/div/button')

        self.errorMessageEmail = (By.XPATH, '//label[text()="Please enter a valid email"]')
        self.errorMessageInvalidPassword = (By.XPATH, '//label[text()="Password must be at least 8 characters and contain at least 1 lowercase, 1 uppercase, 1 number, and 1 symbol"]')
        self.errorMessagePasswordsMustMatch = (By.XPATH, '//label[text()="Passwords must match"]')
        self.errorMessageUserAlreadyExists = (By.XPATH, '//label[text()="User already exists"]')

        self.registerPageURL = r'https://frontend-training-taupe.vercel.app/register'

    def openRegisterPage(self):
        self.driver.get(self.registerPageURL)

    def insertName(self, name):
        self.driver.find_element(*self.nameInput).send_keys(name)

    def insertUsername(self, username):
        self.driver.find_element(*self.usernameInput).send_keys(username)

    def insertEmail(self, email):
        self.driver.find_element(*self.emailInput).send_keys(email)

    def insertPassword(self, password):
        self.driver.find_element(*self.passwordInput).send_keys(password)

    def confirmPassword(self, password):
        self.driver.find_element(*self.confirmPasswordInput).send_keys(password)

    def clickRegisterButton(self):
        self.driver.find_element(*self.registerButton).click()

    def register(self, name, username, email, password):
        self.driver.get(self.registerPageURL)

        self.insertName(name)
        self.insertUsername(username)
        self.insertEmail(email)
        self.insertPassword(password)
        self.confirmPassword(password)

        self.clickRegisterButton()


    def checkSuccessfulRegister(self):
        homePage = HP.HomePage(self.driver)
        return homePage.checkHomePageLoaded()

    def checkErrorMessageEmail(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.errorMessageEmail)
            )
            return True
        except:
            return False

    def checkErrorMessageInvalidPassword(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.errorMessageInvalidPassword)
            )
            return True
        except:
            return False

    def checkErrorMessagePasswordMustMatch(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.errorMessagePasswordsMustMatch)
            )
            return True
        except:
            return False

    def checkErrorMessageUserAlreadyExists(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.errorMessageUserAlreadyExists)
            )
            return True
        except:
            return False
