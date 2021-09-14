import inspect
import logging

import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def gitdemoverifylinkpresence(self, text):
        Wait = WebDriverWait(self.driver, 8)
        Wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectoptionbytext(self, locator, text):
        # dropdown = Select(homepage.getdropdown())
        # dropdown.select_by_visible_text("Male")
        # dropdown.select_by_index(1)
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
