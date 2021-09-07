from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from models.auth import AuthData
from pages.application import Application
import logging

logger = logging.getLogger("moodle")


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    headless_mode = request.config.getoption("--headless")
    logger.info(f"Start moodle {base_url} with headless={headless_mode} mode")
    if headless_mode == "true":
        chrome_options = Options()
        chrome_options.headless = True
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
            base_url
        )
    elif headless_mode == "false":
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install()), base_url
        )
    else:
        raise pytest.UsageError("--headless should be true or false")
    yield fixture
    fixture.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
             "enter 'false' - if not",
    ),
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university/",
        help="enter base url",
    ),
    parser.addoption(
        "--username", action="store", default="vadim951", help="user name"
    ),
    parser.addoption(
        "--password", action="store", default="Testtest@5", help="password"
    ),
    parser.addoption("--firstname", action="store", default="Vadim", help="firstname"),
    parser.addoption("--lastname", action="store", default="Yadutov", help="lastname"),

    parser.addoption(
        "--user_email", action="store", default="yadutovvv@yandex.ru", help="email"
    ),
    parser.addoption(
        "--moodle_net_profile",
        action="store",
        default="student",
        help="moodle_net_profile",
    ),
    parser.addoption("--city", action="store", default="Kazan", help="city"),
    parser.addoption("--about", action="store", default="Iam 28 year", help="about")


@pytest.fixture
def auth(app, request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_auth_page()
    data = AuthData(login=user, password=password)
    app.login.auth(data)


@pytest.fixture
def invalid_auth(app):
    app.open_auth_page()
    data = AuthData.random()
    app.login.auth(data)


# Фикстура задать имя,фамилия и mail по умолчанию
@pytest.fixture
def update_user_info(app, request):
    firstname = request.config.getoption("--firstname")
    lastname = request.config.getoption("--lastname")
    user_email = request.config.getoption("--user_email")
    moodle_net_profile = request.config.getoption("--moodle_net_profile")
    city = request.config.getoption("--city")
    timezone = request.config.getoption("--timezone")
    country_code = request.config.getoption("--country_code")
    about = request.config.getoption("--about")
    personal_data = PersonalData(
        firstname=firstname,
        lastname=lastname,
        user_email=user_email,
        moodle_net_profile=moodle_net_profile,
        city=city,
        timezone=timezone,
        country_code=country_code,
        about=about,
    )
    app.login.update_user()
    app.login.edit_personal_data(personal_data)


# Фикстура для перехода в блок редактирования информации пользователя
@pytest.fixture
def user_info(app):
    app.login.update_user()
