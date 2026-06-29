import pytest
from selenium import webdriver

from utilities.read_properties import read_properties_values

config = read_properties_values("config/configuration.ini")


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default=config["default_browser"],
        help="browser selection"

    )


@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.get(config["base_url"])
    driver.implicitly_wait(int(config["default_timeout"]))
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get('browser_instance')
            if driver:
                screenshot = driver.get_screenshot_as_base64()
                extra.append(pytest_html.extras.image(screenshot, 'base64'))
        report.extras = extra
