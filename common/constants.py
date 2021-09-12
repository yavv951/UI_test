class LoginConstants:
    AUTH_ERROR = "Неверный логин или пароль, попробуйте заново."
    IS_CHANGE_INF = "Изменения сохранены"


class PersonalDataConstants:
    TIMEZONE_VALUES = (
        "Asia/Vladivostok",
        "Australia/Sydney",
        "America/New_York",
        "Africa/Tunis",
        "Europe/Moscow",
        "UTC",
        "99",  # server's timezone
    )
    IMAGE_VALUE = (
        "unknown",
        "allrightsreserved",
        "public",
        "cc",
        "cc-nd",
        "cc-nc-nd",
        "cc-nc",
        "cc-nc-sa",
        "cc-sa",
    )
    IMAGE_NAME = ("my_photo.jpg", "my_photo.png")


class CourseDataConstants:
    YES_NO = ("0", "1")

    VISIBLE = ("0", "1")  # скрыть  # показать

    DAY = (
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
    )

    MONTH = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    START_YEAR = "2021"
    END_YEAR = ("2022", "2023")

    HOUR = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")

    MINUTE = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")

    FORMAT_COURSE = ("singleactivity", "social", "topics", "weeks")

    HIDDENSECTION = ("0", "1")  # В неразвернутом виде  # Полностью невидимы
    COURSEDISPLAY = (
        "0",  # Показывать все секции на одной странице
        "1",  # Показывать одну секцию на странице
    )

    LANGUAGE = ("ru", "en")

    MAXBYTE = ("0", "2097152", "1048576", "512000", "102400", "51200", "10240")
