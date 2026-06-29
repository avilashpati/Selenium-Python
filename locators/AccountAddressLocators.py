from selenium.webdriver.common.by import By


class AccountAddressLocators:
    gender_female = (By.XPATH, "(//input[contains(@id,'id_gender')])[2]")
    account_name = (By.ID,"name")
    account_email = (By.ID, "email")
    account_password = (By.ID, "password")


