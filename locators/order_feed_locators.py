from selenium.webdriver.common.by import By


class OrderFeedLocators:
    """Локаторы для страницы ленты заказов"""

    # Основные элементы страницы
    FEED_PAGE_INDICATOR = (By.XPATH, "//h1[contains(text(), 'Лента заказов') or contains(text(), 'лента заказов')]")
    FEED_CONTENT = (By.CSS_SELECTOR, "[class*='OrderFeed_orderList']")

    # Счетчики заказов
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за всё время')]/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")

    # Разделы
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul")
    ORDERS_IN_PROGRESS_ITEMS = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul/li")
    ORDERS_IN_PROGRESS_TITLE = (By.XPATH, "//p[contains(text(), 'В работе')]")

    # Заказы в ленте
    FIRST_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li")
    ORDER_NUMBER = (By.CLASS_NAME, "text_type_digits-default")

    # Статистика
    STATS_SECTION = (By.CSS_SELECTOR, "[class*='OrderFeed_orderStats']")

    # Альтернативные локаторы (для совместимости)
    ALTERNATIVE_TOTAL_COUNTER = (By.XPATH,
                                 "//p[contains(., 'Выполнено')]/following-sibling::p[contains(., 'за всё время')]")
    ALTERNATIVE_TODAY_COUNTER = (By.XPATH,
                                 "//p[contains(., 'Выполнено')]/following-sibling::p[contains(., 'за сегодня')]")
    TOTAL_ORDERS_TEXT = (By.XPATH, "//*[contains(text(), 'Выполнено за всё время')]")
    TODAY_ORDERS_TEXT = (By.XPATH, "//*[contains(text(), 'Выполнено за сегодня')]")

    # Модальное окно с деталями заказа
    ORDER_MODAL = (By.CLASS_NAME, "Modal_orderBox__1xWdi")
    ORDER_MODAL_NUMBER = (By.CLASS_NAME, "Modal_number__2hyZH")
    ORDER_MODAL_STATUS = (By.CLASS_NAME, "Modal_status__30U0l")
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close__')]")