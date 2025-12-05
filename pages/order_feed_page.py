import allure
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage(BasePage):
    """Класс для работы со страницей ленты заказов"""

    # Локаторы
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за всё время')]/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")

    def __init__(self, driver):
        """Конструктор"""
        super().__init__(driver)

    @allure.step("Открыть страницу ленты заказов")
    def open_feed_page(self):
        """Открыть страницу ленты заказов"""
        self.open()
        return self

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        """Открыть страницу ленты заказов"""
        from config import PAGES
        url = PAGES.get("feed", "https://stellarburgers.education-services.ru/feed")
        print(f"[DEBUG] Открываю страницу ленты заказов: {url}")
        self.driver.get(url)
        time.sleep(3)
        return self

    @allure.step("Проверить, что находимся на странице ленты заказов")
    def is_on_feed_page(self):
        """Проверить, что находимся на странице ленты заказов"""
        try:
            # Проверяем URL
            if "/feed" not in self.driver.current_url:
                return False

            # Проверяем наличие элементов
            page_source = self.driver.page_source.lower()
            keywords = ["выполнено", "лента", "заказов"]
            found = sum(1 for kw in keywords if kw in page_source)

            return found >= 2
        except:
            return False

    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        """Получить количество выполненных заказов за всё время"""
        return self.get_total_orders_counter()

    @allure.step("Получить общее количество заказов")
    def get_total_orders_counter(self):
        """Получить значение счетчика 'Выполнено за всё время'"""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.TOTAL_ORDERS_COUNTER)
            )
            text = element.text.strip()
            # Парсим число
            import re
            numbers = re.findall(r'\d+', text.replace(' ', ''))
            return int(numbers[0]) if numbers else 0
        except:
            return 0

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        """Получить количество выполненных заказов за сегодня"""
        return self.get_today_orders_counter()

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_counter(self):
        """Получить значение счетчика 'Выполнено за сегодня'"""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.TODAY_ORDERS_COUNTER)
            )
            text = element.text.strip()
            # Парсим число
            import re
            numbers = re.findall(r'\d+', text.replace(' ', ''))
            return int(numbers[0]) if numbers else 0
        except:
            return 0

    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        """Получить список заказов в работе"""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ORDERS_IN_PROGRESS_SECTION)
            )
            # Возвращаем текст или пустой список
            text = element.text.strip()
            return [text] if text else []
        except:
            return []

    @allure.step("Ожидать, что URL содержит текст")
    def wait_for_url_contains(self, text, timeout=10):
        """Ждать, что URL содержит определенный текст"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except:
            return False