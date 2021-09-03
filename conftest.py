from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from models.auth import AuthData, PersonalData
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
    parser.addoption("--firstname", action="store", default="Vadim", help="firstname")
    parser.addoption("--lastname", action="store", default="Yadutov", help="lastname")
    parser.addoption(
        "--user_email", action="store", default="yadutovvv@yandex.ru", help="email"
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


# Фикстура задать имя,фамилия и mail по умолчанию
@pytest.fixture
def update_user_info(app, request):
    firstname = request.config.getoption("--firstname")
    lastname = request.config.getoption("--lastname")
    user_email = request.config.getoption("--user_email")
    personal_data = PersonalData(
        firstname=firstname, lastname=lastname, user_email=user_email
    )
    app.login.update_user()
    app.login.edit_personal_data(personal_data)


# Фикстура для перехода в блок редактирования информации пользователя
@pytest.fixture
def user_info(app):
    app.login.update_user()
