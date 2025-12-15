from selenium.webdriver.common.by import By


class OrderFeedLocators:
    """Локаторы для страницы ленты заказов"""

    # Основные индикаторы страницы
    FEED_PAGE_INDICATOR = (By.XPATH, "//h1[contains(text(), 'Лента заказов') or contains(text(), 'лента заказов')]")
    FEED_HEADER = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    FEED_CONTENT = (By.CSS_SELECTOR, "[class*='OrderFeed_orderList']")

    # Счетчики заказов (унифицируем)
    TOTAL_COUNTER_TITLE = (By.XPATH, "//p[contains(text(), 'Выполнено за всё время')]")
    TOTAL_COUNTER_VALUE = (By.XPATH, "//p[contains(text(), 'Выполнено за всё время')]/following-sibling::p")

    TODAY_COUNTER_TITLE = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]")
    TODAY_COUNTER_VALUE = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")

    # Для обратной совместимости
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    # Раздел "В работе" (унифицируем)
    IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(), 'В работе')]")
    IN_PROGRESS_LIST = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul")
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul/li")

    # Для обратной совместимости
    ORDERS_IN_PROGRESS_TITLE = (By.XPATH, "//p[contains(text(), 'В работе')]")
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul")
    ORDERS_IN_PROGRESS_ITEMS = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul/li")

    # Заказы в ленте
    ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li")
    FIRST_ORDER = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_list')]/li)[1]")
    ORDER_NUMBER = (By.CLASS_NAME, "text_type_digits-default")

    # Статистика
    STATS_SECTION = (By.CSS_SELECTOR, "[class*='OrderFeed_orderStats']")

    # Модальное окно
    ORDER_MODAL = (By.CLASS_NAME, "Modal_orderBox__1xWdi")
    ORDER_MODAL_NUMBER = (By.CLASS_NAME, "Modal_number__2hyZH")
    ORDER_MODAL_STATUS = (By.CLASS_NAME, "Modal_status__30U0l")
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close__')]")

    # Динамический локатор для поиска заказа по номеру
    @staticmethod
    def ORDER_BY_NUMBER(order_id):
        return (By.XPATH,
                f"//div[contains(text(), '{order_id}') or contains(@class, 'text_type_digits-default') and contains(text(), '{order_id}')]")
