BASE_URL = "https://stellarburgers.education-services.ru"

# ВЕБ-СТРАНИЦЫ
MAIN_PAGE = f"{BASE_URL}/"
FEED_PAGE = f"{BASE_URL}/feed"
LOGIN_PAGE = f"{BASE_URL}/login"
REGISTER_PAGE = f"{BASE_URL}/register"
PROFILE_PAGE = f"{BASE_URL}/account/profile"

# ТЕСТОВЫЕ ДАННЫЕ
TEST_USER = {
    'name': 'Vinnik',
    'email': 'qaefsf13@hmail.com',
    'password': '123456789'
}

# Для обратной совместимости
MAIN = MAIN_PAGE
FEED = FEED_PAGE
LOGIN = LOGIN_PAGE

# Для обратной совместимости
PAGES = {
    "login": LOGIN_PAGE,
    "register": REGISTER_PAGE,
    "feed": FEED_PAGE,
    "main": MAIN_PAGE,
    "profile": PROFILE_PAGE,
    "forgot_password": FORGOT_PASSWORD_PAGE if 'FORGOT_PASSWORD_PAGE' in locals() else f"{BASE_URL}/forgot-password",
    "reset_password": RESET_PASSWORD_PAGE if 'RESET_PASSWORD_PAGE' in locals() else f"{BASE_URL}/reset-password",
}