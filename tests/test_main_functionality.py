import allure
from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModal
from locators.main_page_locators import MainPageLocators

@allure.feature("Основная функциональность")
@allure.story("Навигация и взаимодействие с элементами")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Проверка перехода на главную страницу при клике на кнопку 'Конструктор' из ленты заказов")
    def test_navigate_to_constructor(self, main_page, order_feed_page):
        """Тест перехода на главную страницу по клику на 'Конструктор'"""
        # 1. Переходим на страницу ленты заказов
        main_page.click_order_feed_button()
        order_feed_page.open()

        # 2. Возвращаемся на главную через кнопку 'Конструктор'
        main_page.click_constructor_button()

        # 3. Проверяем, что находимся на главной странице
        assert main_page.is_element_visible(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.title("Переход по клику на раздел «Лента заказов»")
    @allure.description("Проверка перехода на страницу ленты заказов при клике на соответствующую кнопку в шапке")
    def test_navigate_to_order_feed(self, main_page, order_feed_page):
        """Тест перехода в ленту заказов"""
        # 1. Переходим в ленту заказов
        main_page.click_order_feed_button()
        order_feed_page.open()

        # 2. Проверяем, что находимся на странице ленты заказов
        assert order_feed_page.is_feed_page_loaded()

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    @allure.description(
        "Проверка, что при клике на любой ингредиент открывается модальное окно с его детальной информацией")
    def test_click_ingredient_opens_modal(self, main_page, ingredient_modal):
        """Тест открытия модального окна при клике на ингредиент"""
        # 1. Кликаем на ингредиент
        main_page.click_first_bun_ingredient()

        # 2. Проверяем, что модальное окно открылось
        assert ingredient_modal.is_modal_visible()

    @allure.title("Закрытие модального окна по крестику")
    @allure.description("Проверка закрытия модального окна при клике на кнопку закрытия")
    def test_modal_closes_by_close_button(self, driver, base_url, main_page, ingredient_modal):
        """
        Тест проверяет закрытие модального окна при клике на крестик
        Предусловие: модальное окно уже открыто
        1. Кликаем на крестик для закрытия
        2. Проверяем, что модальное окно закрылось
        """
        # ПРЕДУСЛОВИЕ: открываем модальное окно
        main_page.open()
        main_page.click_first_bun_ingredient()
        assert ingredient_modal.is_opened(), "Модальное окно должно быть открыто перед тестом"

        # ДЕЙСТВИЕ: закрываем модальное окно кликом по крестику
        ingredient_modal.close_by_button()

        # ПРОВЕРКА: модальное окно закрылось
        assert ingredient_modal.is_closed(), "Модальное окно не закрылось после клика на крестик"

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    @allure.description(
        "Проверка, что при перетаскивании ингредиента в конструктор заказа счетчик этого ингредиента увеличивается")
    def test_ingredient_counter_increases(self, driver, main_page):
        """Тест увеличения счетчика ингредиента при добавлении в заказ"""
        # 1. Получаем начальное значение счетчика
        initial_counter = main_page.get_bun_counter_value()

        # 2. Добавляем ингредиент в конструктор
        main_page.drag_bun_to_constructor()

        # 3. Получаем новое значение счетчика
        new_counter = main_page.get_bun_counter_value()

        # 4. Проверяем, что счетчик увеличился
        assert new_counter > initial_counter

    @allure.story("Работа с конструктором бургеров")
    @allure.title("Переключение на раздел «Булки» в конструкторе")
    def test_switch_to_buns_section(self, main_page):
        """Тест переключения на раздел 'Булки'"""
        # Сначала переключаемся на другой раздел
        main_page.click_sauces_section()

        # Затем возвращаемся к булкам
        main_page.click_buns_section()

        # Проверяем результат
        assert main_page.is_buns_section_active()

    @allure.story("Работа с конструктором бургеров")
    @allure.title("Переключение на раздел «Соусы» в конструкторе")
    def test_switch_to_sauces_section(self, main_page):
        """Тест переключения на раздел 'Соусы'"""
        # Переключаемся на раздел Соусы
        main_page.click_sauces_section()

        # Проверяем результат
        assert main_page.is_sauces_section_active()

