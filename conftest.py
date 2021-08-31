from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from models.auth import AuthData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    fixture = Application(webdriver.Chrome(ChromeDriverManager().install()), base_url)
    yield fixture
    fixture.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university/",
        help="enter base url",
    )
    parser.addoption("--username", action="store", default="vadim951", help="user name")
    parser.addoption(
        "--password", action="store", default="Testtest@5", help="password"
    )


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
