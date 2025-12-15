import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@allure.feature("Основная функциональность")
@allure.story("Навигация и взаимодействие с элементами")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, main_page, order_feed_page):
        """Тест перехода на главную страницу по клику на 'Конструктор'"""
        # Переходим на страницу ленты заказов
        main_page.click_order_feed_button()
        order_feed_page.open()

        # Возвращаемся на главную через кнопку 'Конструктор'
        main_page.click_constructor_button()
        assert main_page.is_element_visible(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_navigate_to_order_feed(self, main_page, order_feed_page):
        """Тест перехода в ленту заказов"""
        # 1. Переходим в ленту заказов
        main_page.click_order_feed_button()
        order_feed_page.open()
        assert order_feed_page.is_feed_page()

    @allure.title("Открытие деталей ингредиента")
    def test_ingredient_details_opens(self, main_page: MainPage):
        """Тест проверяет открытие деталей ингредиента при клике"""

        # Открываем главную страницу
        main_page.open()

        # Кликаем на первый ингредиент
        main_page.click_first_ingredient()

        # Проверяем что детали открылись
        assert main_page.is_ingredient_details_opened()

    @allure.title("Закрытие страницы ингредиента")
    def test_close_ingredient_page(self, main_page: MainPage):
        """Тест проверяет, что можно вернуться со страницы ингредиента на главную"""

        # Открываем главную страницу
        main_page.open()

        # Открываем страницу ингредиента
        main_page.click_first_ingredient()

        # Проверяем что страница ингредиента открылась
        assert main_page.is_ingredient_details_opened()

        # Закрываем страницу ингредиента (возвращаемся назад)
        main_page.close_ingredient_details()

        # Проверяем что вернулись на главную
        assert main_page.is_on_main_page()

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_ingredient_counter_increases(self, main_page):
        """Тест увеличения счетчика ингредиента при добавлении в заказ"""
        # Открываем главную страницу
        main_page.open()

        # Получаем начальное значение счетчика
        initial_counter = main_page.get_bun_counter_value()
        main_page.drag_bun_to_constructor()

        # Получаем новое значение счетчика
        new_counter = main_page.get_bun_counter_value()
        assert new_counter > initial_counter, \
            f"Счётчик ингредиента не увеличился! Было: {initial_counter}, Стало: {new_counter}"

    @allure.story("Работа с конструктором бургеров")
    @allure.title("Переключение на раздел «Булки» в конструкторе")
    def test_switch_to_buns_section(self, main_page):
        """Тест переключения на раздел 'Булки'"""

        main_page.open()
        main_page.click_sauces_section()
        main_page.click_buns_section()

        assert main_page.is_buns_section_visible(), "Раздел 'Булки' не активен"

    @allure.story("Работа с конструктором бургеров")
    @allure.title("Переключение на раздел «Соусы» в конструкторе")
    def test_switch_to_sauces_section(self, main_page):
        """Тест переключения на раздел 'Соусы'"""
        main_page.open()
        main_page.click_sauces_section()

        assert main_page.is_sauces_section_visible(), "Раздел 'Соусы' не активен"

    @allure.story("Работа с конструктором бургеров")
    @allure.title("Переключение на раздел «Начинки» в конструкторе")
    def test_switch_to_fillings_section(self, main_page):
        """Тест переключения на раздел 'Начинки'"""
        main_page.open()
        main_page.click_fillings_section()

        assert main_page.is_fillings_section_visible(), \
            "Раздел 'Начинки' не виден после клика"

