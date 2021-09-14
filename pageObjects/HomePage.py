from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    # driver.find_element_by_name("name").send_keys("Manoj")
    namefield = (By.NAME, "name")
    # driver.find_element_by_xpath("//div[@class='container']/form/div[2]/input").send_keys("srimanojskm@gmail.com")
    emailfield = (By.XPATH, "//div[@class='container']/form/div[2]/input")
    # driver.find_element_by_id("exampleInputPassword1").send_keys("samsungj7max12!@")
    passwordfield = (By.ID, "exampleInputPassword1")
    # driver.find_element_by_css_selector("div[class='form-check'] input").click()
    checkbox = (By.CSS_SELECTOR, "div[class='form-check'] input")
    # dropdown = Select(self.driver.find_element_by_css_selector("#exampleFormControlSelect1"))
    dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    # driver.find_element_by_xpath("//input[@id='inlineRadio1']").click()
    radiobutton = (By.XPATH, "//input[@id='inlineRadio1']")
    # driver.find_element_by_css_selector("input.btn.btn-success").click()
    submitbutton = (By.CSS_SELECTOR, "input.btn.btn-success")
    # print(self.driver.find_element_by_css_selector("[class*='alert-success']").text)
    successtext = (By.CSS_SELECTOR, "[class*='alert-success']")

    # Step 2 :
    def shoplink(self):
        self.driver.find_element(*HomePage.shop).click()
        cop = CheckoutPage(self.driver)
        return cop

    def getnamefield(self):
        return self.driver.find_element(*HomePage.namefield)

    def getemailfield(self):
        return self.driver.find_element(*HomePage.emailfield)

    def getpasswordfield(self):
        return self.driver.find_element(*HomePage.passwordfield)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getdropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getradiobutton(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def getsubmitbutton(self):
        return self.driver.find_element(*HomePage.submitbutton)

    def getsuccesstext(self):
        return self.driver.find_element(*HomePage.successtext)
