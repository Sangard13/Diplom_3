import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config import PAGES
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """Класс для работы с главной страницей (конструктор)"""

    def __init__(self, driver):
        """Конструктор"""
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        """Открыть главную страницу"""
        self.open(PAGES["main"])
        self.wait_for_page_load()

    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        """Ждать полной загрузки страницы"""
        try:
            # Используем метод из BasePage
            return self.wait_for_document_ready(timeout=timeout)
        except Exception as e:
            self.logger.error(f"Ошибка при ожидании загрузки страницы: {e}")
            return False

        except Exception as e:
            self.logger.error(f"Ошибка при ожидании загрузки страницы: {e}")
            return False

    @allure.step("Кликнуть на вкладку 'Конструктор'")
    def click_constructor_tab(self):
        """Кликнуть на вкладку Конструктор"""
        self.click_element(MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step("Кликнуть на вкладку 'Лента Заказов'")
    def click_order_feed_tab(self):
        """Кликнуть на вкладку Лента Заказов"""
        self.click_element(MainPageLocators.ORDER_FEED_TAB)

    @allure.step("Проверить, что находимся на главной странице")
    def is_on_main_page(self):
        """Проверить, что находимся на главной странице"""
        try:
            # Проверяем URL
            if not self.wait_for_url_contains("stellarburgers", timeout=5):
                return False

            # Проверяем наличие заголовка
            return self.is_element_visible(MainPageLocators.BURGER_TITLE, timeout=5)

        except Exception as e:
            self.logger.error(f"Ошибка при проверке главной страницы: {e}")
            return False

    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        """Получить все доступные ингредиенты"""
        try:
            return self.wait_for_elements_present(MainPageLocators.INGREDIENT_CARD, timeout=10)
        except Exception as e:
            self.logger.error(f"Ошибка при получении списка ингредиентов: {e}")
            return []

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        """Кликнуть на первый ингредиент"""
        try:
            ingredients = self.get_ingredients()
            if ingredients:
                first_ingredient = self.wait_for_element_clickable(ingredients[0], timeout=10)
                first_ingredient.click()
                return True
            return False

        except Exception as e:
            self.logger.error(f"Ошибка при клике на первый ингредиент: {e}")
            return False

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self, ingredient_element=None):
        """Получить значение счетчика ингредиента"""
        if ingredient_element is None:
            # Найти первый ингредиент
            ingredients = self.get_ingredients()
            if not ingredients:
                return 0
            ingredient_element = ingredients[0]

        try:
            # Ищем счетчик внутри элемента ингредиента
            counter_locator = (By.CSS_SELECTOR, "[class*='counter']")
            counter_elements = self.find_elements_within_element(ingredient_element, counter_locator)

            if counter_elements and self.is_element_visible_in_parent(counter_elements[0], ingredient_element):
                counter_text = counter_elements[0].text.strip()
                # Извлекаем число из текста
                import re
                numbers = re.findall(r'\d+', counter_text)
                return int(numbers[0]) if numbers else 0

        except Exception as e:
            self.logger.debug(f"Счетчик не найден: {e}")

        return 0

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self, use_js=False, ingredient_element=None):
        """Перетащить ингредиент в конструктор"""
        try:
            if ingredient_element is None:
                # Используем стандартное перетаскивание
                if use_js:
                    return self.drag_and_drop_js(
                        MainPageLocators.INGREDIENT_CARD,
                        MainPageLocators.DROP_AREA
                    )
                else:
                    return self.drag_and_drop(
                        MainPageLocators.INGREDIENT_CARD,
                        MainPageLocators.DROP_AREA
                    )
            else:
                # Перетаскиваем конкретный элемент ингредиента
                return self._drag_specific_ingredient(ingredient_element)

        except Exception as e:
            self.logger.error(f"Ошибка при перетаскивании: {e}")
            return False

    def _drag_specific_ingredient(self, ingredient_element):
        """Перетаскивает конкретный элемент ингредиента в конструктор"""
        try:
            # Находим область конструктора
            drop_area = self.wait_for_element_present(MainPageLocators.DROP_AREA, timeout=10)

            # Используем метод drag_and_drop_element из BasePage
            return self.drag_and_drop_element(ingredient_element, drop_area)

        except Exception as e:
            self.logger.error(f"Ошибка при перетаскивании конкретного ингредиента: {e}")
            return False

    @allure.step("Проверить наличие ингредиентов в конструкторе")
    def has_ingredients_in_constructor(self):
        """Проверить, есть ли ингредиенты в конструкторе"""
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_ITEMS, timeout=5)

    @allure.step("Проверить открыто ли модальное окно ингредиента")
    def is_ingredient_modal_opened(self):
        """Проверить, открыто ли модальное окно с деталями ингредиента"""
        return self.is_element_visible(MainPageLocators.MODAL_CONTENT, timeout=5)

    @allure.step("Получить заголовок модального окна ингредиента")
    def get_ingredient_modal_title(self):
        """Получить заголовок модального окна с деталями ингредиента"""
        try:
            element = self.wait_for_element_visible(MainPageLocators.MODAL_TITLE, timeout=5)
            return element.text.strip()
        except Exception as e:
            self.logger.error(f"Ошибка при получении заголовка модального окна: {e}")
            return ""

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        """Закрыть модальное окно с деталями ингредиента"""
        try:
            self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_CONTENT, timeout=5)
            return True
        except Exception as e:
            self.logger.error(f"Ошибка при закрытии модального окна: {e}")
            return False

    @allure.step("Получить первый доступный ингредиент")
    def get_first_available_ingredient(self):
        """Находит первый доступный ингредиент"""
        try:
            # Проверяем, есть ли уже элементы на странице
            if not self.is_element_visible(MainPageLocators.INGREDIENT_CARD, timeout=5):
                self.wait_for_page_load()

            ingredients = self.get_ingredients()
            if ingredients:
                return ingredients[0]

            # Альтернативный поиск, если стандартный локатор не работает
            alternative_selectors = [
                (By.CSS_SELECTOR, "[class*='BurgerIngredient_ingredient']"),
                (By.CSS_SELECTOR, "[class*='ingredient']"),
                (By.CSS_SELECTOR, "section a"),
                (By.CSS_SELECTOR, "section div[class*='card']")
            ]

            for selector in alternative_selectors:
                try:
                    element = self.wait_for_element_present(selector, timeout=2)
                    if element:
                        return element
                except:
                    continue

            return None

        except Exception as e:
            self.logger.error(f"Ошибка при поиске первого ингредиента: {e}")
            return None

    @allure.step("Получить счетчик ингредиента из элемента")
    def get_ingredient_counter_from_element(self, ingredient_element):
        """Получает значение счетчика ингредиента из конкретного элемента"""
        try:
            # Пробуем найти счетчик внутри элемента
            counter_locator = (By.CSS_SELECTOR, "[class*='counter__num'], [class*='counter']")
            counter_elements = self.find_elements_within_element(ingredient_element, counter_locator)

            for element in counter_elements:
                if element.is_displayed():
                    counter_text = element.text.strip()
                    if counter_text:
                        numbers = re.findall(r'\d+', counter_text)
                        return int(numbers[0]) if numbers else 0

            return 0

        except Exception as e:
            self.logger.debug(f"Счетчик не найден в элементе: {e}")
            return 0

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_element=None):
        """Добавляет ингредиент в конструктор и возвращает результат"""
        try:
            if ingredient_element is None:
                ingredient_element = self.get_first_available_ingredient()
                if not ingredient_element:
                    return {'success': False, 'error': 'Ингредиент не найден'}

            # Получаем счетчик до добавления
            counter_before = self.get_ingredient_counter_from_element(ingredient_element)

            # Добавляем ингредиент
            success = self._drag_specific_ingredient(ingredient_element)

            if success:
                # Ждем обновления интерфейса
                self.wait_for_counter_update(ingredient_element, counter_before)

                # Получаем счетчик после добавления
                counter_after = self.get_ingredient_counter_from_element(ingredient_element)

                return {
                    'success': True,
                    'counter_before': counter_before,
                    'counter_after': counter_after,
                    'increased': counter_after > counter_before
                }

            return {'success': False, 'error': 'Не удалось перетащить ингредиент'}

        except Exception as e:
            self.logger.error(f"Ошибка при добавлении ингредиента: {e}")
            return {'success': False, 'error': str(e)}

    @allure.step("Ожидать обновления счетчика")
    def wait_for_counter_update(self, element, initial_value, timeout=5):
        """Ожидает обновления счетчика ингредиента"""

        def counter_updated(driver):
            current_value = self.get_ingredient_counter_from_element(element)
            return current_value != initial_value

        try:
            return self.wait_for_condition(counter_updated, timeout=timeout)
        except:
            return False

    @allure.step("Получить количество ингредиентов в конструкторе")
    def get_constructor_ingredients_count(self):
        """Получает количество ингредиентов в конструкторе"""
        try:
            items = self.wait_for_elements_present(MainPageLocators.CONSTRUCTOR_ITEMS, timeout=5)
            return len(items)
        except Exception as e:
            self.logger.error(f"Ошибка при получении количества ингредиентов: {e}")
            return 0

    @allure.step("Очистить конструктор")
    def clear_constructor(self):
        """Удаляет все ингредиенты из конструктора"""
        try:
            # Ищем кнопки удаления
            delete_locator = (By.CSS_SELECTOR, "[class*='constructor-element__action']")
            delete_buttons = self.find_elements(delete_locator)

            for button in reversed(delete_buttons):  # Удаляем с конца
                try:
                    if button.is_displayed():
                        button.click()
                        self.wait_for_element_staleness(button, timeout=2)
                except:
                    continue

            # Ждем очистки конструктора
            self.wait_for_element_to_disappear(MainPageLocators.CONSTRUCTOR_ITEMS, timeout=5)
            return True

        except Exception as e:
            self.logger.error(f"Ошибка при очистке конструктора: {e}")
            return False