import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages import Login

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.homePageTitle = (By.XPATH, '//h1[text()="Home"]')

        self.profileButton = (By.XPATH, '//button[p/text()="Profile"]')
        self.optionsMenuButton = (By.XPATH, '//div[img[@alt="dot"] and count(img)=3]')
        self.logOutButton = (By.XPATH, '//div[contains(text(), "Log out")]')
        self.confirmLogOutButton = (By.XPATH, '//button[text()="Log out"]')

        self.tweetButton = (By.XPATH, '//button[text()="Tweet"]')
        self.tweetTextArea = (By.CSS_SELECTOR, 'textarea[placeholder="What\'s happening?"]')
        self.publishTweetButton = (By.CSS_SELECTOR, '.sc-ksJisA.eheooK')
        self.fileInput = (By.ID, 'file-input')
        self.previewImageDiv = (By.CSS_SELECTOR, '.sc-fEyylQ.jbGfBU.sc-idyqAC.eULyBW')

        #self.closeIcon = (By.CSS_SELECTOR, 'div.sc-iBAaJG.dqKQza div.sc-ftLKQv.inrQXB button.sc-pqitP.jyAbil > img')
        self.closeIcon = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/button/img')
        self.errorMessageCharsLimit = (By.XPATH, '//label[text()="Post should be between 1 and 240 characters"]')

        self.userProfilePhoto = (By.CSS_SELECTOR, '.sc-csmVar.TfSnt')

        #Deberia ir el mensaje que esperamos que aparezca
        self.errorMessageInvalidFile = (By.XPATH, '//label[text()="Invalid file type"]')
        self.errorMessageMaxImages = (By.XPATH, '//label[text()="Post should have 4 or fewer images"]')

        self.usernameLogged = (By.CSS_SELECTOR, '.sc-ilpitK.hHFWQI')

        self.changeLanguageButton = (By.XPATH, '//div[contains(text(), "Switch to")]')

        self.homePageURL = r'https://frontend-training-taupe.vercel.app/'

    def openHomePage(self):
        self.driver.get(self.homePageURL)

    def clickOptionsMenuButton(self):
        self.driver.find_element(*self.optionsMenuButton).click()

    def clickProfileButton(self):
        self.driver.find_element(*self.profileButton).click()

    def clickLogOutButton(self):
        self.driver.find_element(*self.logOutButton).click()

    def clickConfirmLogOutButton(self):
        self.driver.find_element(*self.confirmLogOutButton).click()

    def clickChangeLanguageButton(self):
        self.driver.find_element(*self.changeLanguageButton).click()

    def clickTweetButton(self):
        self.driver.find_element(*self.tweetButton).click()

    def clickPublishTweetButton(self):
        self.driver.find_element(*self.publishTweetButton).click()

    def clickNewTweetImagePreview(self):
        self.driver.find_element(*self.previewImageDiv).click()

    def clickProfilePhoto(self):
        self.driver.find_element(*self.userProfilePhoto).click()

    def addImageToTweet(self,files):
        self.driver.find_element(*self.fileInput).send_keys(files)

    def addTextToTweet(self, text):
        self.driver.find_element(*self.tweetTextArea).send_keys(text)

    def waitForTextArea(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.tweetTextArea)
            )
        except:
            print('An unexpected error occurred')

    def waitForImagePreview(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.previewImageDiv)
            )
        except:
            print('An unexpected error occurred')

    def waitForProfilePhoto(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.userProfilePhoto)
            )
        except:
            print('An unexpected error occurred')

    def newTweet(self, text):

        self.clickTweetButton()

        WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.tweetTextArea)
        )

        self.addTextToTweet(text)

        self.clickPublishTweetButton()

    def newTweetWithFile(self, text, files):
        self.clickTweetButton()

        WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.tweetTextArea)
        )

        self.addTextToTweet(text)

        self.addImageToTweet(files)

        self.clickPublishTweetButton()




    def logout(self):
        loginPage = Login.LoginPage(self.driver)

        self.openHomePage()
        self.clickOptionsMenuButton()

        WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.logOutButton)
        )

        self.clickLogOutButton()

        WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.confirmLogOutButton)
        )

        self.clickConfirmLogOutButton()

        loginPage.checkLoginPageLoaded()



    def checkHomePageLoaded(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.homePageTitle)
            )

            return True
        except:
            return False

    def checkErrorMessageInvalidFile(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.errorMessageInvalidFile)
            )
            return True
        except:
            return False


    #MUY VERDE, no hay forma de identificar univocamente cada tweet
    def checkTweetSuccessfullyPublished(self, user, tweet):

        tweetXPATH = ('//div[contains(@class, "sc-tIxES jRRtdU") and .//div[contains(text(), "{}")] and .//div[contains(text(), "{}")]]'
                      .format(user, tweet))

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, tweetXPATH))
            )
            return True
        except:
            return False

    def checkUsernameLoggedEqualsTo(self,username):
        return self.driver.find_element(*self.usernameLogged).text == username

    def checkCloseIconOnPreview(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.closeIcon)
            )

            closeIcon = self.driver.find_element(*self.closeIcon)


            return (((closeIcon.size)['width']) == 24 and ((closeIcon.size)['height']) == 24)
        except:
            return False

    def checkErrorMessageCharsLimit(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.errorMessageCharsLimit)
            )
            return True
        except:
            return False


    def checkErrorMessageMaxImages(self):
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located(self.errorMessageMaxImages)
            )
            return True
        except:
            return False