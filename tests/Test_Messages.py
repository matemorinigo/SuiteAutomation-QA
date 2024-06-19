import time

import pytest
from selenium import webdriver
import os
from Pages import Login, Register, HomePage, Profile, Messages

class Test_Message:

    @pytest.fixture
    def Driver(self):
        os.environ['PATH'] += r'C:\Users\Mateo\PycharmProjects\SuiteAutomation-QA\SeleniumDrivers'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        yield driver

        driver.close()
        driver.quit()

    @pytest.fixture
    def LoginUser(self,Driver):
        loginPage = Login.LoginPage(Driver)
        loginPage.login('usuarioMSG','12345Aa!')

    @pytest.fixture
    def LoginUser2(self,Driver):
        loginPage = Login.LoginPage(Driver)
        loginPage.login('usuarioMSG2','12345Aa!')

    def test_sendMessageMore240Chars_022 (self, Driver, LoginUser):

        message="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aut."

        messagesPage = Messages.Messages(Driver)
        messagesPage.openMessagesPage()
        messagesPage.checkMessagesPageLoaded()

        messagesPage.goToUserChat('usuario')

        time.sleep(2)
        messagesPage.writeMessage(message)
        messagesPage.clickSendMessageButton()
        time.sleep(2)
        homePage = HomePage.HomePage(Driver)
        homePage.logout()
        loginPage = Login.LoginPage(Driver)
        loginPage.checkLoginPageLoaded()
        loginPage.login('usuario','12345Aa!')


        homePage.checkHomePageLoaded()
        messagesPage.openMessagesPage()
        messagesPage.checkMessagesPageLoaded()

        messagesPage.goToUserChat('usuarioMSG')
        time.sleep(2)

        #Deberia haber un mensaje de error al enviarlo, pero como no dice nada y el mensaje parece
        #ser enviado, asumo que tiene que ser recibido.
        assert messagesPage.checkMessagesWasReceived(message)


    def test_sendMessageNotFollowing_023(self, Driver, LoginUser2):

        message="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aut."

        messagesPage = Messages.Messages(Driver)
        messagesPage.openMessagesPage()
        messagesPage.checkMessagesPageLoaded()

        messagesPage.goToUserChat('usuario')

        time.sleep(2)
        messagesPage.writeMessage(message)
        messagesPage.clickSendMessageButton()
        time.sleep(2)
        homePage = HomePage.HomePage(Driver)
        homePage.logout()
        loginPage = Login.LoginPage(Driver)
        loginPage.checkLoginPageLoaded()
        loginPage.login('usuario','12345Aa!')


        homePage.checkHomePageLoaded()
        messagesPage.openMessagesPage()
        messagesPage.checkMessagesPageLoaded()


        #Deberia haber una casilla para los mensajes de usuarios que no seguis
        assert messagesPage.checkUserMessagesAppears('usuarioMSG2')

    def test_sendMessageWithImage_028(self, Driver, LoginUser2):

        message="Ut enim isi ut aliquip ex ea commodo consequat. Duis aut."
        imagePath = r'C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\naboo.jpeg'

        messagesPage = Messages.Messages(Driver)
        messagesPage.openMessagesPage()
        messagesPage.checkMessagesPageLoaded()

        messagesPage.goToUserChat('usuario')

        time.sleep(2)
        messagesPage.writeMessage(message)
        messagesPage.addFileToMsg(imagePath)
        messagesPage.clickSendMessageButton()
        time.sleep(2)
        assert messagesPage.checkImageWasSent()

    def test_searchUserMessages_030(self, Driver, LoginUser2):

        messagesPage = Messages.Messages(Driver)
        messagesPage.openMessagesPage()
        messagesPage.checkMessagesPageLoaded()

        messagesPage.searchUser('usuario')

        time.sleep(2)

        assert messagesPage.checkUserMessagesAppears('usuario')

