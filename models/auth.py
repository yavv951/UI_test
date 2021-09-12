import random
from faker import Faker
from common.constants import PersonalDataConstants, CourseDataConstants

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
            firstname=None,
            lastname=None,
            user_email=None,
            moodle_net_profile=None,
            city=None,
            timezone=None,
            country_code=None,
            about=None,
            url=None,
            image_url=None,
            image_inf=None,
            image_name=None
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.user_email = user_email
        self.moodle_net_profile = moodle_net_profile
        self.city = city
        self.timezone = timezone
        self.country_code = country_code
        self.about = about
        self.url = url
        self.image_url = image_url
        self.image_inf = image_inf
        self.image_name = image_name

    @staticmethod
    def random():
        firstname = fake.first_name()
        lastname = fake.last_name()
        user_email = fake.email()
        moodle_net_profile = fake.url()
        city = fake.city()
        timezone = random.choice(PersonalDataConstants.TIMEZONE_VALUES)
        country_code = fake.country_code()
        about = fake.text(max_nb_chars=200)
        url = fake.url()
        image_url = fake.image_url(width=100,height=100)
        image_inf = fake.text(max_nb_chars=30)
        image_name = random.choice(PersonalDataConstants.IMAGE_NAME)
        return PersonalData(
            firstname,
            lastname,
            user_email,
            moodle_net_profile,
            city,
            timezone,
            country_code,
            about,
            url,
            image_url,
            image_inf,
            image_name
        )


class CourseData:
    def __init__(
            self,
            fullname_course=None,
            shortname_course=None,
            visible=None,
            day=None,
            month=None,
            start_year=None,
            end_year=None,
            hour=None,
            minute=None,
            id_number=None,
            about_course=None,
            format_course=None,
            section=None,
            hiddensection=None,
            coursedisplay=None,
            language=None,
            newsitems=None,
            showgrades=None,
            showteports=None,
            yes_or_no=None,
            maxbytes=None,
            flow=None
    ):
        self.fullname_course = fullname_course
        self.shortname_course = shortname_course
        self.visible = visible
        self.day = day
        self.month = month
        self.start_year = start_year
        self.end_year = end_year
        self.hour = hour
        self.minute = minute
        self.id_number = id_number
        self.about_course = about_course
        self.format_course = format_course
        self.section = section
        self.hiddensection = hiddensection
        self.coursedisplay = coursedisplay
        self.language = language
        self.newsitems = newsitems
        self.showgrades = showgrades
        self.showteports = showteports
        self.yes_or_no = yes_or_no
        self.maxbytes = maxbytes
        self.flow = flow

    @staticmethod
    def random():
        fullname_course = fake.text(max_nb_chars=10),
        shortname_course = fake.text(max_nb_chars=5),
        visible = random.choice(CourseDataConstants.VISIBLE),
        day = random.choice(CourseDataConstants.DAY),
        month = random.choice(CourseDataConstants.MONTH),
        start_year = random.choice(CourseDataConstants.START_YEAR),
        end_year = random.choice(CourseDataConstants.END_YEAR),
        hour = random.choice(CourseDataConstants.YES_NO),
        minute = random.choice(CourseDataConstants.YES_NO),
        id_number = random.randint(1, 100),
        about_course = fake.text(max_nb_chars=200),
        format_course = random.choice(CourseDataConstants.FORMAT_COURSE),
        section = random.choice(CourseDataConstants.YES_NO),
        hiddensection = random.choice(CourseDataConstants.HIDDENSECTION),
        coursedisplay = random.choice(CourseDataConstants.COURSEDISPLAY),
        language = random.choice(CourseDataConstants.LANGUAGE),
        newsitems = random.randint(0, 10),
        showgrades = random.choice(CourseDataConstants.YES_NO),
        showteports = random.choice(CourseDataConstants.YES_NO),
        yes_or_no = random.choice(CourseDataConstants.YES_NO),
        maxbytes = random.choice(CourseDataConstants.MAXBYTE),
        flow = 0
        return CourseData(
            fullname_course,
            shortname_course,
            visible,
            day,
            month,
            start_year,
            end_year,
            hour,
            minute,
            id_number,
            about_course,
            format_course,
            section,
            hiddensection,
            coursedisplay,
            language,
            newsitems,
            showgrades,
            showteports,
            yes_or_no,
            maxbytes,
            flow
        )
