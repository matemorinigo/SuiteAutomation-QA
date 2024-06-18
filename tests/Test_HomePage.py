import time

import pytest
from selenium import webdriver
import os
from Pages import Login, Register, HomePage, Profile


class Test_HomePage:

    @pytest.fixture
    def Driver(self):
        os.environ['PATH'] += r'C:\Users\Mateo\PycharmProjects\SuiteAutomation-QA\SeleniumDrivers'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        yield driver

        driver.close()
        driver.quit()

    @pytest.fixture
    def LoginUser(self, Driver):
        loginPage = Login.LoginPage(Driver)
        loginPage.login('usuario','12345Aa!')
        yield

    def test_tweetMoreThan240Chars_011(self, Driver, LoginUser):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()

        homePage.newTweet("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aut. ")

        assert homePage.checkErrorMessageCharsLimit()

    def test_tweetWithImage_012(self, Driver, LoginUser):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()

        tweet = "Lorem ipsum dolor, consecr elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        filePath = r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\alderaan.jpeg"

        homePage.newTweetWithFile(tweet, filePath)

        assert homePage.checkTweetSuccessfullyPublished('usuario', tweet)

    def test_quitImagePreviewOnTweet_013(self, Driver, LoginUser):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()


        filePath = r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\alderaan.jpeg"

        homePage.clickTweetButton()
        homePage.waitForTextArea()
        homePage.addImageToTweet(filePath)
        homePage.waitForImagePreview()
        homePage.clickNewTweetImagePreview()

        assert homePage.checkCloseIconOnPreview()

    def test_addInvalidFile_014(self, Driver, LoginUser):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()


        filePath = r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\alderaan.rar"

        homePage.clickTweetButton()
        homePage.waitForTextArea()
        homePage.addImageToTweet(filePath)

        assert homePage.checkErrorMessageInvalidFile()

    def test_addMultipleImages_015(self, Driver, LoginUser):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()


        filePath = r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\alderaan.jpeg" + '\n' + r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\coruscant.jpg" + '\n' + r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\Dagobah.jpeg" + '\n' + r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\naboo.jpeg"

        homePage.newTweetWithFile("images test", filePath)

        assert homePage.checkTweetSuccessfullyPublished('usuario', "images test")

    def test_addMoreThan4Images_016(self, Driver, LoginUser):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()


        filePath = r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\alderaan.jpeg" + '\n' + r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\coruscant.jpg" + '\n' + r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\Dagobah.jpeg" + '\n' + r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\naboo.jpeg" + '\n' + r"C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\tatooine.png"

        homePage.newTweetWithFile("more than 4 images test", filePath)

        assert homePage.checkErrorMessageMaxImages()

    def test_goToProfilebyProfilePhoto_017(self,Driver,LoginUser):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()

        homePage.waitForProfilePhoto()

        homePage.clickProfilePhoto()

        profilePage = Profile.UserProfile(Driver)
        profilePage.checkProfilePageLoaded()

        assert Driver.current_url != homePage.homePageURL

