import allure
import sys
import os

# Путь для импортов
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@allure.feature("Лента заказов")
@allure.story("Счётчики и отображение заказов")
class TestOrderFeed:
    """Тесты функциональности ленты заказов"""

    @allure.title("6. Счётчик 'Выполнено за всё время' отображается")
    def test_total_counter_displayed(self, driver, feed_page):
        """Тест отображения счетчика 'Выполнено за всё время'"""
        with allure.step("Открыть ленту заказов"):
            feed_page.open()

        with allure.step("Дождаться загрузки страницы"):
            feed_page.wait_for_page_load(timeout=15)

        with allure.step("Проверить отображение счетчика 'Выполнено за всё время'"):
            assert feed_page.is_total_orders_counter_displayed(), \
                "Счетчик 'Выполнено за всё время' не отображается"

        with allure.step("Проверить значение счетчика"):
            total_count = feed_page.get_total_orders_count()
            assert total_count is not None, "Не удалось получить значение счетчика"
            assert total_count != "", "Значение счетчика пустое"

    @allure.title("7. Счётчик 'Выполнено за сегодня' отображается")
    def test_today_counter_displayed(self, feed_page):
        """Тест отображения счетчика 'Выполнено за сегодня'"""
        with allure.step("Открыть ленту заказов"):
            feed_page.open()
            feed_page.wait_for_page_load()

        with allure.step("Проверить отображение счетчика 'Выполнено за сегодня'"):
            assert feed_page.is_today_orders_counter_displayed(), \
                "Счетчик 'Выполнено за сегодня' не отображается"

            today_count = feed_page.get_today_orders_count()
            assert today_count is not None, "Не удалось получить значение счетчика за сегодня"

    @allure.title("8. Раздел 'В работе' отображается")
    def test_orders_in_progress_displayed(self, feed_page):
        """Тест отображения раздела 'В работе'"""
        with allure.step("Открыть ленту заказов"):
            feed_page.open()
            feed_page.wait_for_page_load()

        with allure.step("Проверить отображение раздела 'В работе'"):
            assert feed_page.is_in_progress_section_displayed()

        with allure.step("Получить список заказов в работе"):

            in_progress_orders = feed_page.get_in_progress_orders_list()
            assert isinstance(in_progress_orders, list)