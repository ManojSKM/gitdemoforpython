from pageObjects.HomePage import HomePage
from tests.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        # HomePage
        log = self.getLogger()
        cop = HomePage.shoplink(self)
        print(self.driver.title)
        print(self.driver.current_url)
        # CheckoutPage
        log.info("Getting all the product names")
        pnames = cop.getproductnames()
        i = -1
        for pname in pnames:
            i = i + 1
            pnamestext = pname.text
            #print(pnamestext)
            log.info(pnamestext)
            if pnamestext == "Nokia Edge":
                cop.getproductnamesfooterbutton()[i].click()

        # Validating the product name title, whether selected product name in page 1 is showing in page 2.
        validatingProductName = cop.getcardtitle()
        for titlecheck in validatingProductName:
             if titlecheck == cop.getlinktext():
                print(titlecheck.text)

        cop.getcheckoutbutton().click()
        # ConfirmPage
        cfp = cop.getcheckoutbutton1()
        log.info("Entering country name as ind")
        cfp.gettextboxfield().send_keys("ind")
        self.verifylinkpresence("India") # explicit wait just call the method
        cfp.getlinktextvalue().click()
        cfp.getcheckboxbutton().click()
        print(cfp.getcheckboxbutton().is_displayed())
        cfp.getpurchasebutton().click()
        print(cfp.getalerttext().text)
        SuccessText = cfp.getalerttext().text
        log.info("Text received from application is : "+SuccessText)
        assert "Success! Thank you!" in SuccessText


