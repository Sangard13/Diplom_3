import allure
import re
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    """Класс для работы со страницей ленты заказов"""

    def __init__(self, driver):
        from urls import FEED_PAGE
        super().__init__(driver, FEED_PAGE)
        self.locators = OrderFeedLocators()

    #  Методы навигации

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        """Открыть страницу ленты заказов"""
        super().open()  # Используем self.url из BasePage
        self.wait_for_page_load()

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        """Ожидать загрузки страницы ленты заказов"""
        return self.wait_for(lambda d: self.is_feed_page(), timeout)

    @allure.step("Проверить, что находимся на странице ленты заказов")
    def is_feed_page(self, timeout=5):
        """Проверить URL и наличие элементов"""
        # Проверяем URL
        if "/feed" not in self.driver.current_url:
            return False
        # Проверяем наличие элемента
        return self.is_element_visible(self.locators.FEED_PAGE_INDICATOR, timeout)

    @allure.step("Обновить страницу ленты заказов")
    def refresh(self):
        """Обновить страницу ленты заказов"""
        self.refresh()
        self.wait_for_page_load()

    @allure.step("Дождаться загрузки ленты заказов")
    def wait_for_feed_page_loaded(self, timeout=10):
        """Алиас для wait_for_page_load() для обратной совместимости"""
        return self.wait_for_page_load(timeout)

    #  Методы работы со счетчиками

    @allure.step("Дождаться загрузки счетчиков")
    def wait_for_counters_to_load(self, timeout=10):
        """Дождаться загрузки счетчиков заказов"""
        self.wait_for_element_visible(self.locators.TOTAL_ORDERS_COUNTER, timeout)
        self.wait_for_element_visible(self.locators.TODAY_ORDERS_COUNTER, timeout)

    @allure.step("Проверить отображение счетчика 'Выполнено за все время'")
    def is_total_orders_counter_displayed(self):
        """Проверить, отображается ли счетчик 'Выполнено за все время'"""
        return self.is_element_visible(self.locators.TOTAL_ORDERS_COUNTER, timeout=15)

    @allure.step("Проверить отображение счетчика 'Выполнено за сегодня'")
    def is_today_orders_counter_displayed(self):
        """Проверить, отображается ли счетчик 'Выполнено за сегодня'"""
        return self.is_element_visible(self.locators.TODAY_ORDERS_COUNTER, timeout=10)

    @allure.step("Получить значение счетчика 'Выполнено за всё время'")
    def get_total_orders_count(self):
        """Получить числовое значение счетчика"""
        element = self.find_element(self.locators.TOTAL_ORDERS_COUNTER, timeout=5)
        text = element.text.strip()
        # Извлекаем числа из текста
        numbers = re.findall(r'\d+', text.replace(' ', '').replace(',', ''))
        if numbers:
            return int(numbers[0])
        return 0

    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        """Получить числовое значение счетчика"""
        element = self.find_element(self.locators.TODAY_ORDERS_COUNTER, timeout=5)
        text = element.text.strip()
        numbers = re.findall(r'\d+', text.replace(' ', '').replace(',', ''))
        if numbers:
            return int(numbers[0])
        return 0

    @allure.step("Дождаться отображения счетчика")
    def wait_for_total_counter(self, timeout=15):
        """Дождаться отображения счетчика 'Выполнено за всё время'"""
        # Используем метод из BasePage
        return self.wait_for_element_visible(self.locators.TOTAL_ORDERS_COUNTER, timeout)

    #  Методы работы с заказами "В работе"

    @allure.step("Проверить отображение раздела 'В работе'")
    def is_in_progress_section_displayed(self, timeout=5):
        """Проверить видимость раздела 'В работе'"""
        return self.is_element_visible(self.locators.IN_PROGRESS_SECTION, timeout)

    @allure.step("Получить список заказов в работе")
    def get_in_progress_orders_list(self, timeout=3):
        """Получить список элементов заказов в работе"""
        return self.find_elements(self.locators.IN_PROGRESS_ORDERS, timeout)