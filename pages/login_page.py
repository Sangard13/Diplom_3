import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from urls import LOGIN_PAGE


class LoginPage(BasePage):
    """Класс для работы со страницей авторизации"""

    def __init__(self, driver):
        super().__init__(driver, LOGIN_PAGE)

    @allure.step("Открыть страницу логина")
    def open(self):
        """Открыть страницу логина"""
        super().open()

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        """Ввести email"""
        element = self.find_element(LoginLocators.EMAIL_INPUT)
        element.clear()
        element.send_keys(email)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        """Ввести пароль"""
        element = self.find_element(LoginLocators.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)
        return self

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        """Нажать кнопку 'Войти'"""
        self.click_element(LoginLocators.LOGIN_BUTTON)
        return self

    @allure.step("Авторизоваться с email: {email}")
    def login(self, email, password):
        """
        Полная процедура логина
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Проверить, что страница логина отображается")
    def is_login_page_displayed(self):
        """Проверить, что страница логина отображается"""
        return self.is_element_visible(LoginLocators.LOGIN_BUTTON)

    @allure.step("Перейти на страницу регистрации")
    def go_to_registration(self):
        """Перейти на страницу регистрации"""
        self.click_element(LoginLocators.REGISTER_LINK)
        return self

    @allure.step("Перейти на страницу восстановления пароля")
    def go_to_password_recovery(self):
        """Перейти на страницу восстановления пароля"""
        self.click_element(LoginLocators.RECOVERY_LINK)
        return self