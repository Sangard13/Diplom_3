from selenium.webdriver.common.by import By


class IngredientModalLocators:
    """Локаторы элементов модального окна с деталями ингредиента"""

    # Модальное окно
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")

    # Кнопка закрытия
    CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button")

    # Заголовок
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h3")

    # Детали ингредиента
    INGREDIENT_DETAILS = (By.XPATH, "//div[contains(@class, 'IngredientDetails_details__')]")
    INGREDIENT_NAME = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//p[contains(@class, 'text')]")