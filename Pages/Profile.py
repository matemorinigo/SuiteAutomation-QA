from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages import Login


class MyProfile:

    def __init__(self, driver):
        self.driver = driver
        self.deleteButton = (By.XPATH, '//button[text()="Delete"]')
        self.confirmDeleteButton = (By.XPATH, '//div[@class="sc-iBAaJG dqKQza"]//button[@mode="delete"]')
        self.myProfileURL = r'https://frontend-training-taupe.vercel.app/profile'

    def openProfilePage(self):
        self.driver.get(self.myProfileURL)

    def clickDeleteButton(self):
        self.driver.find_element(*self.deleteButton).click()

    def clickConfirmDeleteButton(self):
        self.driver.find_element(*self.confirmDeleteButton).click()

    def deleteProfile(self):
        loginPage = Login.LoginPage(self.driver)

        self.openProfilePage()

        self.clickDeleteButton()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.confirmDeleteButton)
        )

        self.clickConfirmDeleteButton()

        loginPage.checkSuccessfulLogin()

    def checkUserTweetsAppear(self, user):

        userTweetXPATH = (f'//div[contains(@class, "sc-fcdPlE cMbONl") and text()="{user}"]')

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, userTweetXPATH))
            )
            return True
        except:
            return False

class UserProfile:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.CSS_SELECTOR, '.sc-gJgZMk.bJpLtg')
        self.followButton = (By.XPATH, '//button[contains(text(), "Follow") or contains(text(), "Unfollow")]')


    def openProfilePage(self, url):
        self.driver.get(url)
    def clickFollowButton(self):
        self.driver.find_element(*self.followButton).click()
    def checkProfilePageLoaded(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.username)
            )

            return True
        except:
            return False