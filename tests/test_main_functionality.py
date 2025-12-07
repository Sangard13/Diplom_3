import allure
import pytest
from selenium.webdriver.common.by import By
from pages.ingredient_modal import IngredientModal
from pages.order_feed_page import OrderFeedPage


@allure.feature("Основная функциональность")
@allure.story("Навигация и взаимодействие с элементами")
class TestMainFunctionality:
    """Тесты основной функциональности приложения"""

    @allure.title("1. Переход по клику на «Конструктор»")
    @pytest.mark.smoke
    def test_navigate_to_constructor(self, driver, main_page):
        """
        Тест проверяет переход в конструктор
        """
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            assert main_page.is_on_main_page(), "Главная страница не загрузилась"

        with allure.step("Перейти в ленту заказов"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open_feed_page()
            assert order_feed_page.is_on_feed_page(), "Страница ленты заказов не загрузилась"

        with allure.step("Вернуться на главную через кнопку 'Конструктор'"):
            main_page.click_constructor_tab()
            assert main_page.is_on_main_page(), "Не удалось вернуться на главную страницу"

    @allure.title("2. Переход по клику на раздел «Лента заказов»")
    def test_navigate_to_order_feed(self, main_page):
        """
        Тест проверяет переход в ленту заказов
        """
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            assert main_page.is_on_main_page(), "Главная страница не загрузилась"

        with allure.step("Перейти в ленту заказов через кнопку"):
            main_page.click_order_feed_tab()
            order_feed_page = OrderFeedPage(main_page.driver)
            assert order_feed_page.is_on_feed_page(), "Не удалось перейти на страницу ленты заказов"

    @allure.title("3. Клик на ингредиент открывает всплывающее окно с деталями")
    def test_click_ingredient_opens_modal(self, main_page, ingredient_modal):
        """
        Тест проверяет открытие модального окна при клике на ингредиент
        """
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            assert main_page.is_on_main_page(), "Главная страница не загрузилась"

        with allure.step("Кликнуть на первый ингредиент"):
            assert main_page.click_first_ingredient(), "Не удалось кликнуть на ингредиент"

        with allure.step("Проверить, что модальное окно открылось"):
            assert ingredient_modal.wait_for_modal_open(timeout=5), "Модальное окно не открылось"
            assert ingredient_modal.is_modal_opened(), "Модальное окно не открылось"
            assert ingredient_modal.get_ingredient_name(), "Название ингредиента не отображается"

    @allure.title("4. Всплывающее окно закрывается кликом по крестик")
    @allure.description("Проверка закрытия модального окна при клике на кнопку закрытия")
    def test_close_ingredient_modal_with_x(self, main_page, ingredient_modal):
        """
        Тест проверяет закрытие модального окна при клике на крестик
        """
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            assert main_page.is_on_main_page(), "Главная страница не загрузилась"

        with allure.step("Открыть модальное окно ингредиента"):
            assert main_page.click_first_ingredient(), "Не удалось кликнуть на ингредиент"
            assert ingredient_modal.wait_for_modal_open(timeout=5), "Модальное окно не открылось"

        with allure.step("Закрыть модальное окно кликом по крестику"):
            assert ingredient_modal.click_close_button(), "Не удалось закрыть модальное окно"

        with allure.step("Проверить, что модальное окно закрылось"):
            assert ingredient_modal.is_modal_closed(), "Модальное окно не закрылось"

    @allure.title("5. Проверка функционала счетчика ингредиента")
    def test_ingredient_counter_functionality(self, main_page):
        """
        Тест проверяет наличие и корректность счетчика ингредиента
        """
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            assert main_page.is_on_main_page(), "Главная страница не загрузилась"

        with allure.step("Проверить наличие ингредиентов"):
            ingredients = main_page.get_ingredients()
            assert len(ingredients) > 0, "На странице должны быть ингредиенты"

        with allure.step("Проверить счетчик первого ингредиента"):
            ingredient = ingredients[0]
            counter = main_page.get_ingredient_counter_from_element(ingredient)
            assert counter >= 0, "Счетчик не может быть отрицательным"

    @allure.title("6. Проверка конструктора")
    def test_constructor_available(self, driver, main_page):
        """
        Тест проверяет наличие и доступность конструктора
        """
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            assert main_page.is_on_main_page(), "Главная страница не загрузилась"

        with allure.step("Проверить наличие конструктора"):
            constructor = driver.find_elements(By.CSS_SELECTOR, "[class*='BurgerConstructor']")
            assert len(constructor) > 0, "Конструктор не найден"
            assert constructor[0].is_displayed(), "Конструктор должен быть видимым"

        with allure.step("Проверить наличие ингредиентов"):
            ingredients = main_page.get_ingredients()
            assert len(ingredients) > 0, "Нет ингредиентов для конструктора"