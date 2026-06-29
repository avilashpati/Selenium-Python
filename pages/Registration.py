import time

from selenium.webdriver.common.by import By

from locators.RegistrationLocators import RegistrationPageLocators
from pages.AccountAddress import AccountAddress
from utilities.TestUtils import TestUtils
from utilities.logger import get_logger


class Registration(TestUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.logger = get_logger()
        self.driver = driver
        self.registration_username = RegistrationPageLocators.reg_uname
        self.registration_email = RegistrationPageLocators.reg_umail
        self.registration_button = RegistrationPageLocators.sign_up

    def pass_registration_username(self, registration_username):
        print("{} {}".format("Expected UserName =>", registration_username))
        self.wait_for_page_load()
        self.driver.find_element(*self.registration_username).send_keys(registration_username)
        self.logger.info("Passed registration username")

    def pass_registration_email(self, registration_email):
        self.driver.find_element(*self.registration_email).send_keys(registration_email)
        self.logger.info("Passed registration email")

    def click_signup_button(self):
        self.driver.find_element(*self.registration_button).click()
        self.logger.info("Clicked on Signup button")
        account_address = AccountAddress(self.driver)
        return account_address


