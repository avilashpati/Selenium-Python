from locators.AccountAddressLocators import AccountAddressLocators
from utilities.TestUtils import TestUtils
from utilities.WaitUtils import WaitUtils
from utilities.logger import get_logger


class AccountAddress(TestUtils,WaitUtils):

    def __init__(self,driver):
        TestUtils.__init__(self, driver)
        WaitUtils.__init__(self, driver)
        self.logger = get_logger()
        self.driver = driver
        self.account_gender = AccountAddressLocators.gender_female
        self.account_name = AccountAddressLocators.account_name
        self.account_email = AccountAddressLocators.account_email
        self.account_password = AccountAddressLocators.account_password

    def pass_account_gender(self):
        self.driver.find_element(*self.account_gender).click()
        self.logger.info("Passed account holder gender")

    def assert_auto_populated_account_holder_name(self, expected_name):
        account_holder_name = self.driver.find_element(*self.account_name)
        actual_name = account_holder_name.get_attribute("value")
        assert actual_name == expected_name
        self.logger.info("Account holder name is populated correctly")

    def assert_auto_populated_account_email(self, expected_email):
        account_holder_email = self.driver.find_element(*self.account_email)
        actual_email = account_holder_email.get_attribute("value")
        assert actual_email == expected_email
        self.logger.info("Account holder email is populated correctly")

    def pass_account_password(self, account_pwrd):
        self.driver.find_element(*self.account_password).send_keys(account_pwrd)
        self.logger.info("Entered password")


