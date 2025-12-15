from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы элементов главной страницы"""

    # Навигация в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and p[text()='Конструктор']]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and p[text()='Лента Заказов']]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH,
                               "//a[contains(@class, 'AppHeader_header__link') and .//p[text()='Личный Кабинет']]")

    # Кнопки авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Заголовки
    BURGER_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    PAGE_HEADER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

    # Табы конструктора
    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Булки']]")
    SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Соусы']]")
    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Начинки']]")

    # Ингредиенты
    FIRST_BUN_INGREDIENT = (By.XPATH, "(//section[.//h2[text()='Булки']]//a[contains(@class, 'BurgerIngredient')])[1]")
    BUN_COUNTER = (By.XPATH, "//div[contains(@class, 'counter')]//p")
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    INGREDIENT_PRICE = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_price__')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter')]")

    # Для страницы ингредиента
    INGREDIENT_PAGE_CONTENT = (By.XPATH, "//section[contains(@class, 'ingredient-details')]")
    INGREDIENT_NAME = (By.XPATH, "//h2[contains(@class, 'ingredient-name')]")
    NUTRITION_VALUES = (By.XPATH, "//div[contains(@class, 'nutrition-value')]//p")

    # Конструктор бургеров
    CONSTRUCTOR_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")
    DROP_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    CONSTRUCTOR_ITEMS = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_element')]")

    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_orderNumber')]")

    # Модальное окно ингредиента
    MODAL_OVERLAY = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal_overlay')]"
    )
    MODAL_CONTENT = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal')]"
    )

    # Локаторы для активных состояний разделов
    BUNS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab') and contains(text(), 'Булки')]")
    SAUCES_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab') and contains(text(), 'Соусы')]")
    FILLINGS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab') and contains(text(), 'Начинки')]")

    # XPATH локаторы
    MODAL_CROSS_BUTTON_XPATH = (
        By.XPATH,
        "//div[contains(@class, 'modal')]//button[contains(@class, 'close')] | "
        "//div[@role='dialog']//button[@aria-label='Close']"
    )
    MODAL_XPATH = (
        By.XPATH,
        "//div[contains(@class, 'modal')] | "
        "//div[@role='dialog'] | "
        "//div[contains(@class, 'modal-dialog')]"
    )

    INGREDIENT_CARD = (
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient')]"
    )
    FIRST_INGREDIENT = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    )

    INGREDIENT_TITLE = (By.XPATH, "//h2[contains(@class, 'text_type_main-large')]")
    INGREDIENT_IMAGE = (By.XPATH, "//img[contains(@class, 'IngredientDetails_image')]")
    INGREDIENT_CALORIES = (By.XPATH, "//p[text()='Калории,ккал']/following-sibling::p")
    INGREDIENT_PROTEINS = (By.XPATH, "//p[text()='Белки, г']/following-sibling::p")

    MODAL_INGREDIENT_DETAILS = (
        By.XPATH,
        "//div[contains(@class, 'IngredientDetails_ingredient')]"
    )
    MODAL_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'IngredientDetails_ingredient')]//h3[contains(@class, 'text_type_main-large')]"
    )

    # Крестик для закрытия модального окна ингредиента
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal')]//button[contains(@class, 'Modal_close')]"
    )

    # Детали ингредиента в модальном окне
    INGREDIENT_DETAILS_NAME = (
        By.XPATH,
        "//div[contains(@class, 'IngredientDetails_ingredient')]//p[contains(@class, 'text_type_main-medium')]"
    )
    INGREDIENT_DETAILS_IMAGE = (
        By.XPATH,
        "//div[contains(@class, 'IngredientDetails_ingredient')]//img"
    )

    INGREDIENT_PAGE_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'IngredientDetails_ingredient')]//h3"
    )

    # Nutritional values
    INGREDIENT_DETAILS_CALORIES = (
        By.XPATH,
        "//div[contains(@class, 'IngredientDetails_ingredient')]//p[text()='Калории,ккал']/following-sibling::p"
    )
    INGREDIENT_DETAILS_PROTEINS = (
        By.XPATH,
        "//div[contains(@class, 'IngredientDetails_ingredient')]//p[text()='Белки, г']/following-sibling::p"
    )
    INGREDIENT_DETAILS_FAT = (
        By.XPATH,
        "//div[contains(@class, 'IngredientDetails_ingredient')]//p[text()='Жиры, г']/following-sibling::p"
    )
    INGREDIENT_DETAILS_CARBOHYDRATES = (
        By.XPATH,
        "//div[contains(@class, 'IngredientDetails_ingredient')]//p[text()='Углеводы, г']/following-sibling::p"
    )

    # Секции ингредиентов
    BUNS_SECTION_TITLE = (
        By.XPATH,
        "//h2[text()='Булки']"
    )
    SAUCES_SECTION_TITLE = (
        By.XPATH,
        "//h2[text()='Соусы']"
    )
    FILLINGS_SECTION_TITLE = (
        By.XPATH,
        "//h2[text()='Начинки']"
    )

    INGREDIENT_ITEM_XPATH = (By.XPATH, "//div[contains(@class, 'ingredient') or @data-ingredient]")