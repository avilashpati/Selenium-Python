from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestUtils:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    # def element_to_be_clickable(self,locator, duration=20):
    #     wait = WebDriverWait(self.driver, duration)
    #     return wait.until(expected_conditions.element_to_be_clickable(locator))

    # def wait_for_page_load(self, duration=20):
    #     WebDriverWait(self.driver, duration).until(
    #         lambda driver: driver.execute_script(
    #             "return document.readyState"
    #         ) == "complete"
    #     )

