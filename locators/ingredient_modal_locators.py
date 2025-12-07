from selenium.webdriver.common.by import By


class IngredientModalLocators:
    """Локаторы для модального окна ингредиента"""

    # === ОСНОВНОЕ МОДАЛЬНОЕ ОКНО ===

    # Основной контейнер модального окна
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")  # из первого варианта
    MODAL_CONTAINER = (By.CSS_SELECTOR, "[class*='Modal_modal']")  # из второго варианта

    # Оверлей (фон)
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")  # из первого варианта
    MODAL_OVERLAY_ALT = (By.CSS_SELECTOR, "[class*='Modal_overlay']")  # из второго варианта

    # === ЭЛЕМЕНТЫ УПРАВЛЕНИЯ ===

    # Кнопки закрытия
    CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button")  # из первого варианта
    CLOSE_BUTTON_ALT = (By.CSS_SELECTOR, "button[class*='Modal_close']")  # из второго варианта

    # Универсальные локаторы для кнопок закрытия
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'close') or contains(@class, 'Close')]")

    # === ЗАГОЛОВОК ===

    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h3")  # из первого варианта
    MODAL_TITLE_ALT = (By.CSS_SELECTOR, "[class*='Modal_title']")  # из второго варианта

    # === СОДЕРЖИМОЕ ИНГРЕДИЕНТА ===

    # Детали ингредиента
    INGREDIENT_DETAILS = (By.XPATH, "//div[contains(@class, 'IngredientDetails_details__')]")  # из первого варианта
    INGREDIENT_DETAILS_ALT = (By.CSS_SELECTOR, "[class*='IngredientDetails_details']")  # из второго варианта

    # Название ингредиента
    INGREDIENT_NAME = (By.XPATH,
                       "//div[contains(@class, 'Modal_modal__')]//p[contains(@class, 'text')]")  # из первого варианта
    INGREDIENT_NAME_ALT = (By.CSS_SELECTOR, "[class*='IngredientDetails_name']")  # из второго варианта

    # === ПИЩЕВАЯ ЦЕННОСТЬ ===

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

    # === ИЗОБРАЖЕНИЕ ИНГРЕДИЕНТА ===

    IMAGE_CONTAINER = (By.CSS_SELECTOR, "[class*='IngredientDetails_image']")
    INGREDIENT_IMAGE = (By.CSS_SELECTOR, "[class*='IngredientDetails_image'] img")

    # === АЛЬТЕРНАТИВНЫЕ/УНИВЕРСАЛЬНЫЕ ЛОКАТОРЫ ===

    # Для совместимости и отказоустойчивости
    ALTERNATIVE_MODAL = (By.CSS_SELECTOR, "[role='dialog'], [aria-modal='true']")  # из второго варианта
    ALTERNATIVE_CLOSE = (By.CSS_SELECTOR,
                         "button[aria-label*='закрыть'], button[aria-label*='close']")  # из второго варианта

    # Универсальный поиск любого модального окна
    ANY_MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'modal') or contains(@class, 'Modal')]")

    # === ВСПОМОГАТЕЛЬНЫЕ ЛОКАТОРЫ ===

    # Для ожидания появления/исчезновения
    MODAL_VISIBLE = (By.CSS_SELECTOR,
                     "[class*='Modal_modal'][style*='visibility: visible'], [class*='Modal_modal'][style*='display: block']")
    MODAL_HIDDEN = (By.CSS_SELECTOR,
                    "[class*='Modal_modal'][style*='visibility: hidden'], [class*='Modal_modal'][style*='display: none']")

    # Содержимое модалки
    MODAL_BODY = (By.CSS_SELECTOR, "[class*='Modal_body']")

    # === МЕТОДЫ ДЛЯ УДОБСТВА ===

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

    @classmethod
    def get_nutrition_label(cls, nutrient_type: str) -> tuple:
        """Динамическое получение локатора для названия питательного вещества"""
        nutrient_map = {
            'calories': cls.CALORIES_LABEL,
            'proteins': cls.PROTEINS_LABEL,
            'fats': cls.FATS_LABEL,
            'carbohydrates': cls.CARBOHYDRATES_LABEL
        }
        return nutrient_map.get(nutrient_type.lower(), cls.CALORIES_LABEL)