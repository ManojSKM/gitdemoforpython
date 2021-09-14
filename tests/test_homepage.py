import pytest

from pageObjects.HomePage import HomePage
from tests.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getdata):
        homepage = HomePage(self.driver)
        homepage.getnamefield().send_keys(getdata[0])
        homepage.getemailfield().send_keys(getdata[1])
        homepage.getpasswordfield().send_keys(getdata[2])
        homepage.getcheckbox().click()
        self.selectoptionbytext(homepage.getdropdown(), getdata[3])
        homepage.getradiobutton().click()
        homepage.getsubmitbutton().click()
        print(homepage.getsuccesstext().text)
        message = homepage.getsuccesstext().text
        assert "Success! The Form has" in message
        self.driver.refresh()

    @pytest.fixture(params=[("Manoj", "srimanojskm@gmail.com", "samsungj7max12!@", "Male"), ("Prabala", "prabaskmano@gmail.com", "samsungj7max12!@", "Female"), ("Krishnamoorthy", "krishnamoorthy@gmail.com", "samsungj7max12!@", "Male")])
    def getdata(self, request):
        return request.param


