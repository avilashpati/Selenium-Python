import json

import pytest

from pages.Dashboard import Dashboard
from utilities.logger import get_logger

file_path = "test_data/test_data.json"
with open(file_path) as f:
    test_d = json.load(f)
    test_list = test_d["dataset1"]


@pytest.mark.parametrize("test_list_value",test_list)
def test_register_user(browser_instance,test_list_value):
    driver = browser_instance
    logger = get_logger()
    logger.info("Logger test")
    print("Print test")
    logger.info("Launched browser")
    dashboard = Dashboard(driver)
    logger.info("Printed Dashboard Title")
    registration = dashboard.click_on_signup_or_login()
    registration.pass_registration_username(test_list_value["registration_username"])
    registration.pass_registration_email(test_list_value["registration_email"])
    account_address = registration.click_signup_button()
    account_address.pass_account_gender()
    # account_address.assert_auto_populated_account_holder_name(test_list_value["registration_username"])
    # account_address.assert_auto_populated_account_email(test_list_value["registration_email"])
    # account_address.pass_account_password(test_list_value["registration_password"])


