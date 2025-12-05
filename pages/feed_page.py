import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from config import PAGES  # Добавьте этот импорт


class FeedPage(BasePage):
    """Класс для работы со страницей ленты заказов"""

    @allure.step("Открыть страницу ленты заказов")
    def open_feed_page(self):
        """Открывает страницу ленты заказов"""
        # Используем URL из конфигурации вместо хардкода
        self.open(PAGES["feed"])
        self.wait_for_page_load()

    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        """Ждать полной загрузки страницы"""
        self.wait_for_custom_condition(
            lambda d: d.execute_script("return document.readyState") == "complete",
            timeout=timeout
        )
        # Ждем появления элементов ленты заказов
        try:
            self.wait_for_element_to_be_visible(FeedPageLocators.ORDERS_LIST, timeout=5)
            return True
        except:
            # Проверяем элементы
            if (self.is_element_visible(FeedPageLocators.TOTAL_ORDERS, timeout=3) or
                    self.is_element_visible(FeedPageLocators.TODAY_ORDERS, timeout=3)):
                return True
        return True

    @allure.step("Дождаться видимости элемента")
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        """Ожидать, пока элемент станет видимым"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Получить общее количество заказов")
    def get_total_orders(self):
        """Получает общее количество заказов"""
        try:
            return self.get_text(FeedPageLocators.TOTAL_ORDERS)
        except:
            return "0"

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        """Получает количество заказов за сегодня"""
        try:
            return self.get_text(FeedPageLocators.TODAY_ORDERS)
        except:
            return "0"

    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        """Получает список заказов в работе"""
        try:
            elements = self.find_elements(FeedPageLocators.ORDERS_IN_PROGRESS)
            return [element.text for element in elements if element.text.strip()]
        except:
            return []

    @allure.step("Проверить, отображается ли общий счетчик")
    def is_total_counter_displayed(self):
        """Проверяет, отображается ли счетчик общего количества заказов"""
        return self.is_element_visible(FeedPageLocators.TOTAL_ORDERS, timeout=5)

    @allure.step("Проверить, отображается ли счетчик заказов за сегодня")
    def is_today_counter_displayed(self):
        """Проверяет, отображается ли счетчик заказов за сегодня"""
        return self.is_element_visible(FeedPageLocators.TODAY_ORDERS, timeout=5)

    @allure.step("Проверить, отображаются ли заказы в работе")
    def are_orders_in_progress_displayed(self):
        """Проверяет, отображаются ли заказы в работе"""
        try:
            elements = self.find_elements(FeedPageLocators.ORDERS_IN_PROGRESS)
            return len(elements) > 0
        except:
            return False