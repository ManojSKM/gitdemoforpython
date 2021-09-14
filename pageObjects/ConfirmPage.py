from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    textbox = (By.XPATH, "//input[@id='country']")
    checkbox = (By.CSS_SELECTOR, "div[class*='checkbox']")
    linktext = (By.LINK_TEXT, "India")
    purchasebutton = (By.XPATH, "//input[@value='Purchase']")
    alerttext = (By.CSS_SELECTOR, "div[class*='alert-dismissible']")

    def gettextboxfield(self):
        return self.driver.find_element(*ConfirmPage.textbox)

    def getcheckboxbutton(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getlinktextvalue(self):
        return self.driver.find_element(*ConfirmPage.linktext)

    def getpurchasebutton(self):
        return self.driver.find_element(*ConfirmPage.purchasebutton)

    def getalerttext(self):
        return self.driver.find_element(*ConfirmPage.alerttext)

