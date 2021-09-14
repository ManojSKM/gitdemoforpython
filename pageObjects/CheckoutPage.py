from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    productnames = (By.XPATH, "//div[@class='card h-100']/div/h4")
    productnamesfooterbutton = (By.XPATH, "//div[@class='card h-100']/div[2]")
    checkoutbutton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutbutton1 = (By.CSS_SELECTOR, "button[class*='btn-success']")
    cardtitle = (By.XPATH, "//h4[@class='card-title']/a")
    linktext = (By.LINK_TEXT, "Nokia Edge")

    def getproductnames(self):
        return self.driver.find_elements(*CheckoutPage.productnames)

    def getproductnamesfooterbutton(self):
        return self.driver.find_elements(*CheckoutPage.productnamesfooterbutton)

    def getcheckoutbutton(self):
        return self.driver.find_element(*CheckoutPage.checkoutbutton)

    def getcardtitle(self):
        return self.driver.find_elements(*CheckoutPage.cardtitle)

    def getlinktext(self):
        return self.driver.find_element(*CheckoutPage.linktext)

    # Step 2
    def getcheckoutbutton1(self):
        self.driver.find_element(*CheckoutPage.checkoutbutton1).click()
        cfp = ConfirmPage(self.driver)
        return cfp



