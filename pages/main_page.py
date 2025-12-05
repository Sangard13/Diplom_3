import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config import PAGES
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MainPage(BasePage):
    """Класс для работы с главной страницей (конструктор)"""

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        """Открыть главную страницу"""
        self.open(PAGES["main"])
        self.wait_for_page_load()

    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        """Ждать полной загрузки страницы"""
        self.wait_for_custom_condition(
            lambda d: d.execute_script("return document.readyState") == "complete",
            timeout=timeout
        )
        # Ждем появления заголовка или ингредиента
        if self.is_element_visible(MainPageLocators.BURGER_TITLE, timeout=5):
            return True
        elif self.is_element_visible(MainPageLocators.INGREDIENT_CARD, timeout=5):
            return True
        return True

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
        return self.is_element_visible(MainPageLocators.BURGER_TITLE)

    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        """Получить все доступные ингредиенты"""
        return self.find_elements(MainPageLocators.INGREDIENT_CARD)

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        """Кликнуть на первый ингредиент"""
        ingredients = self.get_ingredients()
        if ingredients:
            ingredients[0].click()
            return True
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
            counter_elements = ingredient_element.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
            if counter_elements and counter_elements[0].is_displayed():
                counter_text = counter_elements[0].text.strip()
                # Извлекаем число из текста
                import re
                numbers = re.findall(r'\d+', counter_text)
                return int(numbers[0]) if numbers else 0
        except:
            pass
        return 0

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self, use_js=False, ingredient_element=None):
        """Перетащить ингредиент в конструктор"""
        try:
            if ingredient_element is None:
                # Используем стандартное перетаскивание
                if use_js:
                    self.drag_and_drop_js(
                        MainPageLocators.INGREDIENT_CARD,
                        MainPageLocators.DROP_AREA
                    )
                else:
                    self.drag_and_drop(
                        MainPageLocators.INGREDIENT_CARD,
                        MainPageLocators.DROP_AREA
                    )
            else:
                # Перетаскиваем конкретный элемент ингредиента
                return self._drag_specific_ingredient(ingredient_element)
            return True
        except Exception as e:
            print(f"Ошибка при перетаскивании: {e}")
            return False

    def _drag_specific_ingredient(self, ingredient_element):
        """Перетаскивает конкретный элемент ингредиента в конструктор"""
        try:
            # Находим область конструктора
            drop_area = self.find_element(MainPageLocators.DROP_AREA)

            # Используем ActionChains для перетаскивания
            actions = ActionChains(self.driver)
            actions.click_and_hold(ingredient_element) \
                .move_to_element(drop_area) \
                .release(drop_area) \
                .perform()
            return True
        except Exception as e:
            print(f"Ошибка при перетаскивании конкретного ингредиента: {e}")
            return False

    @allure.step("Проверить наличие ингредиентов в конструкторе")
    def has_ingredients_in_constructor(self):
        """Проверить, есть ли ингредиенты в конструкторе"""
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_ITEMS)

    @allure.step("Проверить открыто ли модальное окно ингредиента")
    def is_ingredient_modal_opened(self):
        """Проверить, открыто ли модальное окно с деталями ингредиента"""
        return self.is_element_visible(MainPageLocators.MODAL_CONTENT)

    @allure.step("Получить заголовок модального окна ингредиента")
    def get_ingredient_modal_title(self):
        """Получить заголовок модального окна с деталями ингредиента"""
        try:
            return self.get_text(MainPageLocators.MODAL_TITLE)
        except:
            return ""

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        """Закрыть модальное окно с деталями ингредиента"""
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_to_disappear(MainPageLocators.MODAL_CONTENT)


    @allure.step("Получить первый доступный ингредиент")
    def get_first_available_ingredient(self):
        """Находит первый доступный ингредиент"""
        # Проверяем, есть ли уже элементы на странице
        if not self.is_element_visible(MainPageLocators.INGREDIENT_CARD, timeout=5):
            self.wait_for_page_load()

        ingredients = self.get_ingredients()
        if ingredients:
            return ingredients[0]

        # Альтернативный поиск, если стандартный локатор не работает
        try:
            return self.find_element((By.CSS_SELECTOR, "[class*='BurgerIngredient_ingredient']"))
        except:
            # Еще одна попытка с другим селектором
            return self.find_element((By.CSS_SELECTOR, "[class*='ingredient']"))

    @allure.step("Получить счетчик ингредиента из элемента")
    def get_ingredient_counter_from_element(self, ingredient_element):
        """Получает значение счетчика ингредиента из конкретного элемента"""
        try:
            # Пробуем найти счетчик внутри элемента
            counter_element = ingredient_element.find_element(By.CSS_SELECTOR, "[class*='counter__num']")
            if counter_element and counter_element.is_displayed():
                counter_text = counter_element.text.strip()
                if counter_text:
                    return int(counter_text)
        except:
            pass

        # Альтернативный поиск
        try:
            # Ищем счетчик по другому классу
            counter_element = ingredient_element.find_element(By.XPATH,
                                                              ".//*[contains(@class, 'counter')]//*[contains(text(), '1') or contains(text(), '2') or contains(text(), '3')]")
            if counter_element:
                return int(counter_element.text.strip())
        except:
            pass

        return 0

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_element=None):
        """Добавляет ингредиент в конструктор и возвращает результат"""
        if ingredient_element is None:
            ingredient_element = self.get_first_available_ingredient()

        # Получаем счетчик до добавления
        counter_before = self.get_ingredient_counter_from_element(ingredient_element)

        # Добавляем ингредиент
        success = self._drag_specific_ingredient(ingredient_element)

        if success:
            # Ждем обновления интерфейса
            self.wait_for_element_to_update(ingredient_element)

            # Получаем счетчик после добавления
            counter_after = self.get_ingredient_counter_from_element(ingredient_element)

            return {
                'success': True,
                'counter_before': counter_before,
                'counter_after': counter_after,
                'increased': counter_after > counter_before
            }

        return {'success': False}

    @allure.step("Ожидать обновления элемента")
    def wait_for_element_to_update(self, element, timeout=3):
        """Ожидает обновления элемента (например, счетчика)"""
        try:
            import time
            time.sleep(1)

            # Или ждем изменения класса/атрибута
            initial_class = element.get_attribute("class")
            WebDriverWait(self.driver, timeout).until(
                lambda d: element.get_attribute("class") != initial_class
            )
        except:
            import time
            time.sleep(1)

    @allure.step("Получить количество ингредиентов в конструкторе")
    def get_constructor_ingredients_count(self):
        """Получает количество ингредиентов в конструкторе"""
        try:
            items = self.find_elements(MainPageLocators.CONSTRUCTOR_ITEMS)
            return len(items)
        except:
            return 0

    @allure.step("Очистить конструктор")
    def clear_constructor(self):
        """Удаляет все ингредиенты из конструктора"""
        try:
            # Ищем кнопки удаления или закрытия для каждого ингредиента
            delete_buttons = self.find_elements((By.CSS_SELECTOR, "[class*='constructor-element__action']"))
            for button in delete_buttons:
                try:
                    button.click()
                except:
                    pass

            # Ждем очистки
            self.wait_for_element_to_disappear(MainPageLocators.CONSTRUCTOR_ITEMS, timeout=5)
            return True
        except:
            return False