from selenium.webdriver.common.by import By


class FeedPageLocators:
    """Локаторы элементов страницы ленты заказов"""

    # Заголовок страницы
    FEED_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")

    # Счётчики
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")

    # Номер заказа в списке заказов (шаблон)
    @staticmethod
    def order_number(order_num):
        """Шаблон для поиска номера заказа"""
        return (By.XPATH, f"//p[contains(text(), '#{order_num}')]")

    # Заказы в работе
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]//li")