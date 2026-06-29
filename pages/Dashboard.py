from selenium.webdriver.common.by import By

from locators.DashboardLocators import DashBoardLocators
from pages.Registration import Registration
from utilities.TestUtils import TestUtils
from utilities.logger import get_logger


class Dashboard(TestUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.logger = get_logger()
        self.driver = driver
        self.click_signup_or_login = DashBoardLocators.signup_or_login

    def click_on_signup_or_login(self):
        element = self.element_to_be_clickable(self.click_signup_or_login)
        element.click()
        self.logger.info("Clicked on Signup or Login button in dashboard")
        registration = Registration(self.driver)
        return registration
