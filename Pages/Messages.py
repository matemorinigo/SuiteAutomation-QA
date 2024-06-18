from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages import Login


class Messages:

    def __init__(self, driver):
        self.driver = driver
        self.messagesURL = r'https://frontend-training-taupe.vercel.app/message'
        self.userMessageXPATH = r'//div[contains(@class, "sc-iFgQXl iIMuwa") and contains(text(), "{}")]'
        self.messagesText = (By.XPATH, '//div[text()="Messages"]')
        self.messageInput = (By.XPATH, '//div[contains(@class, "sc-htehxa ezMGfe")]//input[@placeholder="Start a new message"]')
        self.sendMessageButton = (By.CSS_SELECTOR, 'img[alt="message-send-button"]')
        self.messageXPATH = (By.XPATH, '//div[contains(@class, "sc-jmxxdg bVCWwt") and text()="{}"]')

    def openMessagesPage(self):
        self.driver.get(self.messagesURL)

    def checkMessagesPageLoaded(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.messagesText)
            )
        except:
            print('An unexpected error ocurred')

    def goToUserChat(self, user):
        xpath = self.userMessageXPATH.format(user)

        self.driver.find_element(By.XPATH, xpath).click()

    def clickSendMessageButton(self):
        self.driver.find_element(*self.sendMessageButton).click()

    def writeMessage(self, text):
        self.driver.find_element(*self.messageInput).send_keys(text)

    def checkUserMessagesAppears(self, user):
        try:
            userXPATH = self.userMessageXPATH.format(user)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH,userXPATH))
            )
            return True
        except:
            return False

    def checkMessagesWasReceived(self, text):
        try:
            textXPATH = self.userMessageXPATH.format(text)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH,textXPATH))
            )
            return True
        except:
            return False