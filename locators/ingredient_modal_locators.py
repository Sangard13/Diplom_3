from selenium.webdriver.common.by import By


class IngredientModalLocators:
    """Локаторы для модального окна ингредиента"""

    # Основной контейнер модального окна
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CONTAINER = (By.CSS_SELECTOR, "[class*='Modal_modal']")

    # Оверлей (фон)
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")
    MODAL_OVERLAY_ALT = (By.CSS_SELECTOR, "[class*='Modal_overlay']")

    # Кнопки закрытия
    CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button")
    CLOSE_BUTTON_ALT = (By.CSS_SELECTOR, "button[class*='Modal_close']")

    # Универсальные локаторы для кнопок закрытия
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'close') or contains(@class, 'Close')]")

    # ЗАГОЛОВОК

    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h3")
    MODAL_TITLE_ALT = (By.CSS_SELECTOR, "[class*='Modal_title']")

    # Детали ингредиента
    INGREDIENT_DETAILS = (By.XPATH, "//div[contains(@class, 'IngredientDetails_details__')]")
    INGREDIENT_DETAILS_ALT = (By.CSS_SELECTOR, "[class*='IngredientDetails_details']")

    # Название ингредиента
    INGREDIENT_NAME = (By.XPATH,
                       "//div[contains(@class, 'Modal_modal__')]//p[contains(@class, 'text')]")
    INGREDIENT_NAME_ALT = (By.CSS_SELECTOR, "[class*='IngredientDetails_name']")

    # Значения из второго варианта
    CALORIES_VALUE = (By.XPATH, "//p[contains(text(), 'Калории')]/following-sibling::p[1]")
    PROTEINS_VALUE = (By.XPATH, "//p[contains(text(), 'Белки')]/following-sibling::p[1]")
    FATS_VALUE = (By.XPATH, "//p[contains(text(), 'Жиры')]/following-sibling::p[1]")
    CARBOHYDRATES_VALUE = (By.XPATH, "//p[contains(text(), 'Углеводы')]/following-sibling::p[1]")

    # Названия категорий пищевой ценности
    CALORIES_LABEL = (By.XPATH, "//p[contains(text(), 'Калории')]")
    PROTEINS_LABEL = (By.XPATH, "//p[contains(text(), 'Белки')]")
    FATS_LABEL = (By.XPATH, "//p[contains(text(), 'Жиры')]")
    CARBOHYDRATES_LABEL = (By.XPATH, "//p[contains(text(), 'Углеводы')]")

    # Контейнер с пищевой ценностью
    NUTRITION_CONTAINER = (By.CSS_SELECTOR, "[class*='IngredientDetails_nutrition']")

    # ИЗОБРАЖЕНИЕ ИНГРЕДИЕНТА

    IMAGE_CONTAINER = (By.CSS_SELECTOR, "[class*='IngredientDetails_image']")
    INGREDIENT_IMAGE = (By.CSS_SELECTOR, "[class*='IngredientDetails_image'] img")

    # Для совместимости и отказоустойчивости
    ALTERNATIVE_MODAL = (By.CSS_SELECTOR, "[role='dialog'], [aria-modal='true']")
    ALTERNATIVE_CLOSE = (By.CSS_SELECTOR,
                         "button[aria-label*='закрыть'], button[aria-label*='close']")

    # Универсальный поиск любого модального окна
    ANY_MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'modal') or contains(@class, 'Modal')]")

    #  ВСПОМОГАТЕЛЬНЫЕ ЛОКАТОРЫ

    # Для ожидания появления/исчезновения
    MODAL_VISIBLE = (By.CSS_SELECTOR,
                     "[class*='Modal_modal'][style*='visibility: visible'], [class*='Modal_modal'][style*='display: block']")
    MODAL_HIDDEN = (By.CSS_SELECTOR,
                    "[class*='Modal_modal'][style*='visibility: hidden'], [class*='Modal_modal'][style*='display: none']")

    # Содержимое модалки
    MODAL_BODY = (By.CSS_SELECTOR, "[class*='Modal_body']")

    @classmethod
    def get_nutrition_value(cls, nutrient_type: str) -> tuple:
        """Динамическое получение локатора для значения питательного вещества"""
        nutrient_map = {
            'calories': cls.CALORIES_VALUE,
            'proteins': cls.PROTEINS_VALUE,
            'fats': cls.FATS_VALUE,
            'carbohydrates': cls.CARBOHYDRATES_VALUE
        }
        return nutrient_map.get(nutrient_type.lower(), cls.CALORIES_VALUE)

