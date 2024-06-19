import time

import pytest
from selenium import webdriver
import os
from Pages import Login, Register, HomePage, Profile


class Test_Profile:

    @pytest.fixture
    def Driver(self):
        os.environ['PATH'] += r'C:\Users\Mateo\PycharmProjects\SuiteAutomation-QA\SeleniumDrivers'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        yield driver

        driver.close()
        driver.quit()

    @pytest.fixture
    def LoginSender(self,Driver):
        loginPage = Login.LoginPage(Driver)
        loginPage.login('usuario2','12345Aa!')



    @pytest.fixture
    def LoginUser(self, Driver):
        loginPage = Login.LoginPage(Driver)
        loginPage.login('usuario2','12345Aa!')
        yield

    @pytest.fixture
    def TweetSomething(self, Driver):
        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()
        homePage.checkHomePageLoaded()
        homePage.newTweet('New Tweet')
        time.sleep(2)
        yield


    @pytest.fixture
    def RegisterUser(self, Driver):
        registerPage = Register.RegisterPage(Driver)
        registerPage.register("usuariocp021","usuariocp021","usuariocp021@example.com","12345Aa!")

    def test_followUser_018(self,Driver,LoginUser):

        userProfile = Profile.UserProfile(Driver)
        userProfile.openProfilePage(r'https://frontend-training-taupe.vercel.app/profile?user=df085a46-789d-4ac8-b742-a345bc09bb79')

        userProfile.checkProfilePageLoaded()

        userProfile.clickFollowButton()

        time.sleep(1)

        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()

        homePage.checkHomePageLoaded()
        homePage.clickFollowingSection()

        assert homePage.checkUserTweetsAppear('usuario')

        userProfile.openProfilePage(r'https://frontend-training-taupe.vercel.app/profile?user=df085a46-789d-4ac8-b742-a345bc09bb79')

        userProfile.checkProfilePageLoaded()
        userProfile.clickFollowButton()


    def test_unfollowUser_019(self,Driver,LoginUser):

        userProfile = Profile.UserProfile(Driver)
        userProfile.openProfilePage(r'https://frontend-training-taupe.vercel.app/profile?user=df085a46-789d-4ac8-b742-a345bc09bb79')

        userProfile.checkProfilePageLoaded()

        userProfile.clickFollowButton()

        time.sleep(2)

        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()

        userProfile.openProfilePage(r'https://frontend-training-taupe.vercel.app/profile?user=df085a46-789d-4ac8-b742-a345bc09bb79')

        userProfile.checkProfilePageLoaded()

        userProfile.clickFollowButton()
        time.sleep(2)

        homePage.openHomePage()
        homePage.checkHomePageLoaded()
        homePage.clickFollowingSection()

        assert homePage.checkUserTweetsDoesntAppear('usuario')

    def test_deleteProfile_021(self,Driver,RegisterUser):

        homePage = HomePage.HomePage(Driver)
        homePage.openHomePage()
        homePage.checkHomePageLoaded()

        homePage.newTweet("DeletedTweet")

        myProfile = Profile.MyProfile(Driver)
        myProfile.deleteProfile()

        loginPage = Login.LoginPage(Driver)
        loginPage.checkLoginPageLoaded()

        loginPage.login('usuario','12345Aa!')
        homePage.openHomePage()
        homePage.checkHomePageLoaded()

        assert homePage.checkUserTweetsDoesntAppear('usuariocp021')

    def test_deleteTweet_031(self,Driver,LoginUser,TweetSomething):
        myProfile = Profile.MyProfile(Driver)
        myProfile.openProfilePage()
        myProfile.checkProfilePageLoaded()
        myProfile.clickTweetOptions()
        time.sleep(2)
        myProfile.clickDeleteTweet()
        time.sleep(2)
        myProfile.clickConfirmDeleteTweet()
        time.sleep(2)

        myProfile.checkProfilePageLoaded()

        assert myProfile.checkUserTweetsAppear('usuario2')














