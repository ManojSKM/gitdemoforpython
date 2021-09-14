import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageMultipleTestData import HomePageMultipleTestData
from tests.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getdata):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First name is : " +getdata["First Name"])
        homepage.getnamefield().send_keys(getdata["First Name"])
        log.info("Email is : " +getdata["Email"])
        homepage.getemailfield().send_keys(getdata["Email"])
        log.info("PWD is : " +getdata["Password"])
        homepage.getpasswordfield().send_keys(getdata["Password"])
        homepage.getcheckbox().click()
        log.info("Gender is :  " +getdata["Gender"])
        self.selectoptionbytext(homepage.getdropdown(), getdata["Gender"])
        homepage.getradiobutton().click()
        homepage.getsubmitbutton().click()
        print(homepage.getsuccesstext().text)
        message = homepage.getsuccesstext().text
        assert "Success! The Form has" in message
        self.driver.refresh()

    #@pytest.fixture(params=HomePageMultipleTestData.test_homepage_data)
    #def getdata(self, request):
     #   return request.param

    @pytest.fixture(params=HomePageMultipleTestData.gettestdata("TestCase2"))
    def getdata(self, request):
        return request.param


