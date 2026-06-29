from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    reg_uname = (By.XPATH, "//input[@data-qa='signup-name']")
    reg_umail = (By.XPATH, "//input[@data-qa='signup-email']")
    sign_up = (By.XPATH,"//button[text()='Signup']")