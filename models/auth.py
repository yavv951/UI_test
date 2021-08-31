import random

from faker import Faker

from UI_test.common.constants import PersonalDataConstants

fake = Faker()


class AuthData:
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()
        return AuthData(login, password)


class PersonalData:
    def __init__(
        self,
        first_name=None,
        last_name=None,
        email=None,
        moodle_net_profile=None,
        city=None,
        timezone=None,
        country_code=None,
        about=None,
        url=None,
        image_url=None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.moodle_net_profile = moodle_net_profile
        self.city = city
        self.timezone = timezone
        self.country_code = country_code
        self.about = about
        self.url = url
        self.image_url = image_url

    @staticmethod
    def random():
        first_name = fake.first_name()
        last_name = fake.last_name()
        user_email = fake.email()
        moodle_net_profile = fake.url()
        city = fake.city_name()
        timezone = random.choice(PersonalDataConstants.TIMEZONE_VALUES)
        country_code = fake.country_code()
        about = fake.text(max_nb_chars=200)
        url = fake.url()
        image_url = fake.image_url()
        return PersonalData(
            first_name,
            last_name,
            user_email,
            moodle_net_profile,
            city,
            timezone,
            country_code,
            about,
            url,
            image_url,
        )
