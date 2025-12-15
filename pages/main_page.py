import allure
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    """Класс для работы с главной страницей (конструктор)"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
        self.base_url = "https://stellarburgers.education-services.ru/"

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.base_url)
        return self

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL страницы"""
        return self.driver.current_url

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor_button(self):
        """Кликнуть на кнопку Конструктор в навигации"""
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)
        return self

    @allure.step("Кликнуть на кнопку 'Лента Заказов' с помощью JavaScript")
    def click_order_feed_button(self):
        """Кликнуть на кнопку Лента Заказов в навигации"""
        self.click_element(self.locators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        """Кликнуть на первый ингредиент"""
        self.click_element(self.locators.FIRST_INGREDIENT, timeout=10)
        return self

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

    @allure.step("Проверить открытие страницы ингредиента")
    def is_ingredient_page_opened(self):
        """Проверить что открылась страница ингредиента"""
        return "/ingredient/" in self.driver.current_url

    @allure.step("Проверить открытие деталей ингредиента")
    def is_ingredient_details_opened(self):
        """Проверить что детали ингредиента открыты"""
        # Проверяем URL
        if "/ingredient/" not in self.driver.current_url:
            return False

        # Проверяем наличие заголовка
        title = self.find_element(self.locators.INGREDIENT_TITLE, timeout=5)
        return title.is_displayed()

    @allure.step("Получить название ингредиента")
    def get_ingredient_name(self):
        """Получить название ингредиента"""
        # Если не на странице ингредиента, возвращаем None
        if "/ingredient/" not in self.driver.current_url:
            return None

        title = self.find_element(self.locators.INGREDIENT_TITLE, timeout=5)
        return title.text if title.is_displayed() else None

    @allure.step("Проверить видимость изображения ингредиента")
    def is_ingredient_image_visible(self):
        """Проверить что изображение ингредиента отображается"""
        # Если не на странице ингредиента, возвращаем False
        if "/ingredient/" not in self.driver.current_url:
            return False

        image = self.find_element(self.locators.INGREDIENT_IMAGE, timeout=5)
        return image.is_displayed()

    @allure.step("Получить детали ингредиента")
    def get_ingredient_details(self):
        """Получить детали ингредиента"""
        details = {}

        # Название ингредиента
        details['name'] = self.find_element(self.locators.INGREDIENT_PAGE_TITLE).text

        return details

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        """Прокрутить страницу к элементу"""
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_loaded(self, timeout=10):
        """Дождаться загрузки главной страницы"""
        # Проверяем что основные элементы загрузились
        return self.wait_for_element_visible(self.locators.PAGE_HEADER, timeout)

    @allure.step("Проверить отображение модального окна на странице ингредиента")
    def is_modal_displayed_on_ingredient_page(self, timeout=10):
        """Проверить что на странице ингредиента отображается модальное окно"""
        # Проверяем что мы на странице ингредиента
        if not self.is_ingredient_page_opened():
            return False

        # Проверяем наличие видимого модального окна
        return self.is_element_visible(self.locators.MODAL_OVERLAY, timeout)

    @allure.step("Закрыть модальное окно кликом по крестику")
    def close_modal_with_cross(self):
        """Закрыть модальное окно кликом по крестику"""
        self.click_element(self.locators.MODAL_CLOSE_BUTTON, timeout=10)
        return self

    @allure.step("Закрыть страницу ингредиента")
    def close_ingredient_details(self):
        """Закрыть страницу ингредиента (вернуться назад)"""
        self.driver.back()

        # Ждем возврата на главную
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(self.base_url)
        )
        return self

    @allure.step("Проверить что на главной странице")
    def is_on_main_page(self):
        """Проверить что находимся на главной странице"""
        return self.driver.current_url == self.base_url

    @allure.step("Дождаться загрузки страницы ингредиента")
    def wait_for_ingredient_page_loaded(self, timeout=15):
        """Дождаться загрузки страницы ингредиента"""
        # Ждем загрузки URL с /ingredient/
        self.wait_for_url_contains("/ingredient/", timeout)
        self.wait_for_element_visible(self.locators.INGREDIENT_PAGE_CONTENT, timeout)

    @allure.step("Дождаться открытия модального окна")
    def wait_for_modal_opened(self, timeout=10):
        """Дождаться открытия модального окна"""
        self.find_element(self.locators.MODAL_CONTENT, timeout=20)
        return self

    @allure.step("Дождаться закрытия модального окна")
    def wait_for_modal_closed(self, timeout=10):
        """Дождаться закрытия модального окна"""
        self.wait_for_element_to_disappear(self.locators.MODAL_CONTENT, timeout=timeout)
        return self

    @allure.step("Проверить отображение модального окна")
    def is_modal_displayed(self):
        """Проверить, отображается ли модальное окно"""
        elements = self.driver.find_elements(*self.locators.MODAL_CONTENT)
        if elements:
            return elements[0].is_displayed()
        return False

    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        """Получить заголовок модального окна ингредиента"""
        return self.get_element_text(self.locators.MODAL_TITLE)

    @allure.step("Проверить наличие ингредиентов на странице")
    def has_ingredients(self):
        """Проверить, есть ли ингредиенты на странице"""
        elements = self.driver.find_elements(*self.locators.FIRST_INGREDIENT)
        return len(elements) > 0