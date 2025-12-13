import allure
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModal
from locators.main_page_locators import MainPageLocators


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

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_click_ingredient_opens_modal(self, main_page, driver):
        """Тест открытия модального окна при клике на ингредиент"""
        # Открываем главную страницу
        main_page.open()
        main_page.click_first_bun_ingredient()
        modal = IngredientModal(main_page.driver)
        assert modal.is_modal_visible()

    @allure.title("Закрытие модального окна по крестику")
    def test_ingredient_modal_closes(self, driver):
        """Тест закрытия модального окна при клике на крестик"""
        # Создаем экземпляры страниц
        main_page = MainPage(driver)
        modal = IngredientModal(driver)

        # Открываем главную страницу
        main_page.open()
        main_page.click_first_bun_ingredient()
        assert modal.is_modal_opened(), "Модальное окно не открылось"

        # Закрываем модальное окно кликом по крестику
        modal.click_close_button()
        assert modal.is_modal_closed(), "Модальное окно не закрылось после клика на крестик"

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