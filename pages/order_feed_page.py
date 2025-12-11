import allure
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    """Класс для работы со страницей ленты заказов"""

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.locators = OrderFeedLocators()

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        """Открыть страницу ленты заказов"""
        super().open("/feed")

    @allure.step("Проверить загрузку страницы ленты заказов")
    def is_feed_page_loaded(self):
        """Проверить загрузку страницы ленты заказов"""
        return self.is_element_visible(self.locators.FEED_PAGE_INDICATOR)

    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        """Получить количество выполненных заказов за всё время"""
        element = self.find_element(self.locators.TOTAL_ORDERS_COUNTER)
        return element.text

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        """Получить количество выполненных заказов за сегодня"""
        element = self.find_element(self.locators.TODAY_ORDERS_COUNTER)
        return element.text

    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        """Получить список заказов в работе"""
        elements = self.find_elements(self.locators.ORDERS_IN_PROGRESS_SECTION)
        return [element.text for element in elements]

    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order(self):
        """Кликнуть на первый заказ в ленте"""
        element = self.find_element(self.locators.FIRST_ORDER)
        element.click()

    @allure.step("Проверить отображение счетчика 'Выполнено за всё время'")
    def is_total_counter_displayed(self):
        """Проверить, отображается ли счетчик 'Выполнено за всё время'"""
        return self.is_element_visible(self.locators.TOTAL_ORDERS_TEXT)

    @allure.step("Проверить отображение счетчика 'Выполнено за сегодня'")
    def is_today_counter_displayed(self):
        """Проверить, отображается ли счетчик 'Выполнено за сегодня'"""
        return self.is_element_visible(self.locators.TODAY_ORDERS_TEXT)

    @allure.step("Проверить отображение раздела 'В работе'")
    def is_in_progress_section_displayed(self):
        """Проверить, отображается ли раздел 'В работе'"""
        return self.is_element_visible(self.locators.ORDERS_IN_PROGRESS_TITLE)

    @allure.step("Получить количество заказов в работе")
    def get_orders_in_progress_count(self):
        """Получить количество заказов в работе"""
        elements = self.find_elements(self.locators.ORDERS_IN_PROGRESS_ITEMS)
        return len(elements)

    @allure.step("Получить общее количество заказов на странице")
    def get_all_orders_count(self):
        """Получить общее количество заказов, отображаемых на странице"""
        elements = self.find_elements(self.locators.ORDER_LIST)
        return len(elements)

    @allure.step("Проверить, что счетчики содержат числа")
    def are_counters_have_numbers(self):
        """Проверить, что счетчики содержат числовые значения"""
        # Используем find_elements вместо find_element
        total_elements = self.find_elements(self.locators.TOTAL_ORDERS_COUNTER)
        today_elements = self.find_elements(self.locators.TODAY_ORDERS_COUNTER)

        # Проверяем, что элементы найдены
        if not total_elements or not today_elements:
            return False

        total_element = total_elements[0]
        today_element = today_elements[0]

        # Проверяем отображение
        if not total_element.is_displayed() or not today_element.is_displayed():
            return False

        # Получаем текст
        total_text = total_element.text
        today_text = today_element.text

        # Проверяем наличие текста
        if not total_text or not today_text:
            return False

        # Проверяем наличие цифр
        has_total_numbers = bool(re.search(r'\d', total_text))
        has_today_numbers = bool(re.search(r'\d', today_text))

        return has_total_numbers and has_today_numbers

    @allure.step("Дождаться загрузки счетчиков")
    def wait_for_counters_to_load(self, timeout=10):
        """Дождаться загрузки счетчиков заказов"""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.locators.TOTAL_ORDERS_COUNTER)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.locators.TODAY_ORDERS_COUNTER)
        )

    @allure.step("Дождаться появления заказов в ленте")
    def wait_for_orders_to_load(self, timeout=10):
        """Дождаться появления заказов в ленте"""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.locators.ORDER_LIST)
        )

    @allure.step("Проверить, что номер заказа отображается")
    def is_order_number_displayed(self, order_index=0):
        """Проверить, что номер заказа отображается"""
        elements = self.find_elements(self.locators.ORDER_NUMBER)

        # find_elements возвращает пустой список, если элементы не найдены
        if not elements or len(elements) == 0:
            return False

        if len(elements) <= order_index:
            return False

        element = elements[order_index]

        # Дополнительная проверка, что элемент доступен
        if not element:
            return False

        return element.is_displayed() and bool(element.text.strip())

