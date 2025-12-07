import allure
import re
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderFeedPage(BasePage):
    """Класс для работы со страницей ленты заказов"""

    # Локаторы
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за всё время')]/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")
    FEED_PAGE_INDICATOR = (By.XPATH, "//h1[contains(text(), 'Лента заказов') or contains(text(), 'лента заказов')]")

    def __init__(self, driver):
        """Конструктор"""
        super().__init__(driver)

    @allure.step("Открыть страницу ленты заказов")
    def open_feed_page(self):
        """Открыть страницу ленты заказов"""
        return self.open()

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        """Открыть страницу ленты заказов"""
        from config import PAGES
        url = PAGES.get("feed", "https://stellarburgers.education-services.ru/feed")
        self.driver.get(url)
        self.wait_for_page_load()
        # Ждем появления индикатора страницы ленты заказов
        self.wait_for_element_present(self.FEED_PAGE_INDICATOR)
        return self

    @allure.step("Проверить, что находимся на странице ленты заказов")
    def is_on_feed_page(self):
        """Проверить, что находимся на странице ленты заказов"""
        try:
            # Проверяем URL
            current_url = self.get_current_url()
            is_feed_url = "/feed" in current_url

            # Проверяем наличие заголовка или ключевых слов
            keywords = ["выполнено", "лента", "заказов"]
            page_source = self.driver.page_source.lower()
            matches = sum(1 for kw in keywords if kw in page_source)

            return is_feed_url and matches >= 2
        except Exception as e:
            self.logger.error(f"Ошибка при проверке страницы ленты заказов: {e}")
            return False

    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        """Получить количество выполненных заказов за всё время"""
        return self.get_total_orders_counter()

    @allure.step("Получить общее количество заказов")
    def get_total_orders_counter(self):
        """Получить значение счетчика 'Выполнено за всё время'"""
        try:
            element = self.wait_for_element_visible(self.TOTAL_ORDERS_COUNTER, timeout=10)
            text = element.text.strip()

            # Парсим число
            numbers = re.findall(r'\d+', text.replace(' ', ''))
            count = int(numbers[0]) if numbers else 0
            return count

        except Exception as e:
            self.logger.error(f"Ошибка при получении общего количества заказов: {e}")
            return 0

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        """Получить количество выполненных заказов за сегодня"""
        return self.get_today_orders_counter()

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_counter(self):
        """Получить значение счетчика 'Выполнено за сегодня'"""
        try:
            element = self.wait_for_element_visible(self.TODAY_ORDERS_COUNTER, timeout=10)
            text = element.text.strip()

            # Парсим число
            numbers = re.findall(r'\d+', text.replace(' ', ''))
            count = int(numbers[0]) if numbers else 0
            return count

        except Exception as e:
            self.logger.error(f"Ошибка при получении количества заказов за сегодня: {e}")
            return 0

    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        """Получить список заказов в работе"""
        try:
            element = self.wait_for_element_present(self.ORDERS_IN_PROGRESS_SECTION, timeout=10)
            text = element.text.strip()
            return [text] if text else []

        except Exception as e:
            self.logger.error(f"Ошибка при получении заказов в работе: {e}")
            return []