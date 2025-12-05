from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы элементов главной страницы"""

    # Навигация в шапке
    CONSTRUCTOR_TAB = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and p[text()='Конструктор']]")
    ORDER_FEED_TAB = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and p[text()='Лента Заказов']]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH,
                               "//a[contains(@class, 'AppHeader_header__link') and .//p[text()='Личный Кабинет']]")

    # Кнопки авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Заголовки
    BURGER_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

    # Табы конструктора
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Булки']]")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Соусы']]")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Начинки']]")

    # Секции ингредиентов
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")

    # Ингредиенты
    INGREDIENT_CARD = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_NAME = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_name')]")
    INGREDIENT_PRICE = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_price__')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter')]")

    # Конструктор бургеров
    CONSTRUCTOR_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")
    DROP_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    CONSTRUCTOR_ITEMS = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_element')]")

    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_orderNumber')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")

    # Модальное окно ингредиента
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h3")

    # Алиасы для совместимости
    CONSTRUCTOR_BUTTON = CONSTRUCTOR_TAB
    ORDER_FEED_BUTTON = ORDER_FEED_TAB
    ORDER_FEED_BTN = ORDER_FEED_TAB
    PLACE_ORDER_BUTTON = ORDER_BUTTON