from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitUtils:

    def __init__(self, driver):
        self.driver = driver

    def presence_of_element(self, locator, duration=10):
        wait = WebDriverWait(self.driver, duration)
        return wait.until(expected_conditions.presence_of_element_located(locator))

    def visibility_of_element(self, locator, duration=10):
        wait = WebDriverWait(self.driver, duration)
        return wait.until(expected_conditions.visibility_of_element_located(locator))

    def element_to_be_clickable(self,locator, duration=10):
        wait = WebDriverWait(self.driver, duration)
        return wait.until(expected_conditions.element_to_be_clickable(locator))

    def presence_of_all_elements(self, locator, duration=10):
        wait = WebDriverWait(self.driver, duration)
        return wait.until(expected_conditions.presence_of_all_elements_located(locator))

    def wait_for_page_load(self, duration=20):
        WebDriverWait(self.driver, duration).until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )
