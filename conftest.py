import pytest
from selenium import webdriver

"""Set up webdriver."""
options = webdriver.FirefoxOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

geckodriver_path = '/snap/bin/geckodriver'  # specify the path to your geckodriver
driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    if language:
        print("\nstart browser for test..")
        options.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(service=driver_service, options=options)
    else:
        raise pytest.UsageError("--language must be filled")
    options.set_preference('intl.accept_languages', language)
    yield browser
    print("\nquit browser..")
    browser.quit()
