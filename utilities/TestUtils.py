class TestUtils:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
