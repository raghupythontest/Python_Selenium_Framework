import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver=None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_option = webdriver.ChromeOptions()
        # headless mode means, It will run without opening the chrome app.Basically it will run in backround.
        # chrome_option.add_argument("headless")
        chrome_option.add_argument("--start-maximized")
        chrome_option.add_argument("--ignore-certificate-errors")

        service_obj = Service("C:/Development/chromedriver")
        # integrating chromeOptions to webdriver
        driver = webdriver.Chrome(service=service_obj, options=chrome_option)

    elif browser_name == "firefox":
        pass

    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
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
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
