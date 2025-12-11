import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    """Класс для работы со страницей ленты заказов"""

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.locators = FeedPageLocators()

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        """Открыть страницу ленты заказов"""
        super().open("/feed")

    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        """Получить общее количество заказов"""
        element = self.find_element(self.locators.TOTAL_ORDERS_COUNTER)
        return element.text

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        """Получить количество заказов за сегодня"""
        element = self.find_element(self.locators.TODAY_ORDERS_COUNTER)
        return element.text

    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        """Получает список заказов в работе"""
        elements = self.find_elements(self.locators.ORDERS_IN_PROGRESS)
        return [element.text.strip() for element in elements if element.text.strip()]