import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Класс для работы с главной страницей (конструктор)"""

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.locators = MainPageLocators()

    @allure.step("Открыть главную страницу")
    def open(self):
        """Открыть главную страницу"""
        super().open("/")

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor_button(self):
        """Кликнуть на кнопку Конструктор в навигации"""
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку 'Лента Заказов'")
    def click_order_feed_button(self):
        """Кликнуть на кнопку Лента Заказов в навигации"""
        self.click_element(self.locators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на первую булку")
    def click_first_bun_ingredient(self):
        """Кликнуть на первую булку для открытия модального окна"""
        self.click_element(self.locators.FIRST_BUN_INGREDIENT)

    @allure.step("Получить значение счетчика у булки")
    def get_bun_counter_value(self):
        """Получить значение счетчика у булки"""
        element = self.find_element(self.locators.BUN_COUNTER)
        text = element.text.strip()
        return int(text) if text.isdigit() else 0

    @allure.step("Перетащить булку в конструктор")
    def drag_bun_to_constructor(self):
        """Перетащить булку в конструктор"""
        self.drag_and_drop(
            self.locators.FIRST_BUN_INGREDIENT,
            self.locators.CONSTRUCTOR_DROP_AREA
        )

    @allure.step("Кликнуть на раздел 'Булки'")
    def click_buns_section(self):
        """Кликнуть на раздел 'Булки'"""
        element = self.find_element(self.locators.BUNS_SECTION)
        element.click()

    @allure.step("Кликнуть на раздел 'Соусы'")
    def click_sauces_section(self):
        """Кликнуть на раздел 'Соусы'"""
        # Используем JavaScript для обхода перекрытия
        element = self.find_element(self.locators.SAUCES_SECTION)
        element.click()

    @allure.step("Кликнуть на раздел 'Начинки'")
    def click_fillings_section(self):
        """Кликнуть на раздел 'Начинки'"""
        element = self.find_element(self.locators.FILLINGS_SECTION)
        element.click()

