from selenium.webdriver.common.by import By


class LoginLocators:
    """Локаторы для страницы авторизации"""

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")