from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.homePageTitle = (By.XPATH, '//h1[text()="Home"]')

        self.profileButton = (By.XPATH, '//button[p/text()="Profile"]')

        self.homePageURL = r'https://frontend-training-taupe.vercel.app/'

    def clickProfileButton(self):
        self.driver.find_element(*self.profileButton).click()

    def checkHomePageLoaded(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.homePageTitle)
            )

            return True
        except:
            return False