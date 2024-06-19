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
        homePage = HomePage.HomePage(Driver)
        loginPage.login('usuario','12345Aa!')
        yield

    @pytest.fixture
    def TweetSomething(self, Driver):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()
        homePage.checkHomePageLoaded()
        homePage.newTweet('New Tweet')
        time.sleep(2)
        yield
    def test_likeTweet_024(self,Driver,LoginUser, TweetSomething):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()
        homePage.checkHomePageLoaded()

        likesBefore = homePage.getTweetLikes()
        time.sleep(2)

        #Hago un doble click, porque con el driver a veces funciona con doble click y a veces no.
        #Desde la web tambien a veces pasa lo mismo
        homePage.likeTweet()
        time.sleep(2)
        homePage.likeTweet()
        time.sleep(10)

        assert likesBefore < homePage.getTweetLikes()
        time.sleep(5)

        homePage.likeTweet()
        time.sleep(2)

    def test_retweetTweet_025(self,Driver,LoginUser, TweetSomething):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()
        homePage.checkHomePageLoaded()

        tweetUsername = homePage.getTweetUsername()
        retweetsBefore = homePage.getTweetRetweets()
        time.sleep(2)
        homePage.retweetTweet()
        time.sleep(2)
        homePage.retweetTweet()
        time.sleep(2)

        assert retweetsBefore < homePage.getTweetRetweets()
        time.sleep(5)

        profilePage = Profile.MyProfile(Driver)
        profilePage.openProfilePage()

        assert profilePage.checkUserTweetsAppear(tweetUsername)

        homePage.openHomePage()
        homePage.checkHomePageLoaded()

        homePage.retweetTweet()
        time.sleep(2)



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

    def test_followYourself_020(self,Driver):
        #Me parece redundante hacer el registro de 2 usuarios,
        #por lo que cree dos usuarios usuariocp0201 y usuariocp0202 que para que este cp funcione
        #deben estar creados. Asi mismo, en la especificacion de caso de prueba aparece como precondicion

        loginPage = Login.LoginPage(Driver)
        loginPage.openLoginPage()
        loginPage.login('usuariocp0201','12345Aa!')

        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()
        homePage.checkHomePageLoaded()

        assert not(homePage.checkUserAppearsOnWhoToFollow('usuariocp0201'))


    def test_addImageToReplyTweet_026(self,Driver,LoginUser):
        imagePath = r'C:\Users\Mateo\OneDrive\Desktop\imagenesSirius\naboo.jpeg'

        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()
        homePage.checkHomePageLoaded()

        homePage.clickCommentButton()
        homePage.waitForTextArea()

        homePage.addImageToTweet(imagePath)
        homePage.addTextToReply("pruebaReply")

        time.sleep(2)

        assert homePage.checkImagePreview()

        homePage.clickPublishTweetButton()
        homePage.clickCloseRepliesButton()
        time.sleep(2)

        homePage.checkHomePageLoaded()
        homePage.clickCommentButton()
        homePage.waitForTextArea()

        assert homePage.checkUserReplyAppear('usuario')

    def test_repliesOnTweet_027(self,Driver,LoginUser):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()
        homePage.checkHomePageLoaded()

        homePage.clickCommentButton()
        homePage.waitForTextArea()

        homePage.addTextToReply("pruebaReply")

        time.sleep(2)
        homePage.clickPublishTweetButton()
        time.sleep(2)
        homePage.clickCloseRepliesButton()

        homePage.checkHomePageLoaded()
        homePage.clickTweet()

        assert homePage.checkRepliesAppear()

    def test_searchBar_032(self,Driver, LoginUser):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()
        homePage.checkHomePageLoaded()

        urlBefore = Driver.current_url

        homePage.searchOnTwitter('tweet')
        time.sleep(2)

        assert urlBefore != Driver.current_url





