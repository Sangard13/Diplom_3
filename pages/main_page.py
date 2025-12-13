import allure
from urls import MAIN_PAGE
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Класс для работы с главной страницей (конструктор)"""

    @allure.step("Создание MainPage")
    def __init__(self, driver):
        super().__init__(driver, MAIN_PAGE)
        self.locators = MainPageLocators()

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor_button(self):
        """Кликнуть на кнопку Конструктор в навигации"""
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку 'Лента Заказов' с помощью JavaScript")
    def click_order_feed_button(self):
        """Кликнуть на кнопку Лента Заказов в навигации"""
        self.click_element_with_js(self.locators.ORDER_FEED_BUTTON)

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
        element = self.find_element(self.locators.SAUCES_SECTION)
        element.click()

    @allure.step("Кликнуть на раздел 'Начинки'")
    def click_fillings_section(self):
        """Кликнуть на раздел 'Начинки'"""
        element = self.find_element(self.locators.FILLINGS_SECTION)
        element.click()

    @allure.step("Проверить видимость раздела 'Булки'")
    def is_buns_section_visible(self):
        return self.is_element_visible(self.locators.BUNS_SECTION, timeout=3)

    @allure.step("Проверить видимость раздела 'Соусы'")
    def is_sauces_section_visible(self):
        return self.is_element_visible(self.locators.SAUCES_SECTION, timeout=3)

    @allure.step("Проверить что раздел 'Начинки' отображается")
    def is_fillings_section_visible(self):
        """Просто проверяем что раздел виден (без проверки активности)"""
        return self.is_element_visible(self.locators.FILLINGS_SECTION, timeout=3)