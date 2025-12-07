import allure
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotInteractableException,
    StaleElementReferenceException
)


class IngredientModal(BasePage):
    """
       Компонент для работы с модальным окном деталей ингредиента

       Этот компонент используется поверх других страниц (главная страница, лента заказов)
       когда пользователь кликает на ингредиент для просмотра деталей.
       """

    """Класс для работы с модальным окном деталей ингредиента"""

    def __init__(self, driver):
        """Конструктор"""
        super().__init__(driver)
        self.locators = IngredientModalLocators()

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self):
        """Проверить, что модальное окно открыто"""
        try:
            return self.is_element_visible(self.locators.MODAL_CONTAINER, timeout=5)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.warning(f"Модальное окно не открыто: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при проверке открытия модального окна: {e}")
            raise

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        """Проверить, что модальное окно закрыто"""
        try:
            # Проверяем, что элемент исчез
            return self.wait_for_element_to_disappear(
                self.locators.MODAL_CONTAINER,
                timeout=5
            )
        except TimeoutException:
            # Если элемент не исчез за указанное время
            self.logger.warning("Модальное окно не закрылось за указанное время")
            return False
        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при проверке закрытия модального окна: {e}")
            raise

    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        """Получить текст заголовка модального окна"""
        try:
            element = self.wait_for_element_visible(
                self.locators.MODAL_TITLE,
                timeout=5
            )
            return element.text.strip()
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.warning(f"Не удалось получить заголовок модального окна: {e}")
            return ""
        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при получении заголовка: {e}")
            raise

    @allure.step("Получить название ингредиента")
    def get_ingredient_name(self):
        """Получить название ингредиента"""
        try:
            element = self.wait_for_element_visible(
                self.locators.INGREDIENT_NAME,
                timeout=5
            )
            return element.text.strip()
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.warning(f"Не удалось получить название ингредиента: {e}")
            return ""
        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при получении названия: {e}")
            raise

    @allure.step("Проверить наличие деталей ингредиента")
    def is_ingredient_details_visible(self):
        """Проверить, отображаются ли детали ингредиента"""
        try:
            return self.is_element_visible(
                self.locators.INGREDIENT_DETAILS,
                timeout=5
            )
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.warning(f"Детали ингредиента не отображаются: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при проверке деталей: {e}")
            raise

    @allure.step("Получить пищевую ценность ингредиента")
    def get_nutritional_value(self):
        """Получить пищевую ценность ингредиента"""
        nutritional_data = {}

        try:
            # Калории
            if self.is_element_visible(self.locators.CALORIES_VALUE, timeout=3):
                element = self.find_element(self.locators.CALORIES_VALUE)
                nutritional_data['calories'] = self._extract_number_from_text(element.text)

            # Белки
            if self.is_element_visible(self.locators.PROTEINS_VALUE, timeout=3):
                element = self.find_element(self.locators.PROTEINS_VALUE)
                nutritional_data['proteins'] = self._extract_number_from_text(element.text)

            # Жиры
            if self.is_element_visible(self.locators.FATS_VALUE, timeout=3):
                element = self.find_element(self.locators.FATS_VALUE)
                nutritional_data['fats'] = self._extract_number_from_text(element.text)

            # Углеводы
            if self.is_element_visible(self.locators.CARBOHYDRATES_VALUE, timeout=3):
                element = self.find_element(self.locators.CARBOHYDRATES_VALUE)
                nutritional_data['carbohydrates'] = self._extract_number_from_text(element.text)

        except (TimeoutException, NoSuchElementException) as e:
            self.logger.warning(f"Не удалось получить пищевую ценность: {e}")
        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при получении пищевой ценности: {e}")
            # В этом случае лучше поднять исключение, так как это может быть серьёзная проблема
            raise

        return nutritional_data

    def _extract_number_from_text(self, text):
        """Извлечь число из текста"""
        try:
            numbers = re.findall(r'\d+', text)
            return int(numbers[0]) if numbers else 0
        except (IndexError, ValueError) as e:
            self.logger.warning(f"Не удалось извлечь число из текста '{text}': {e}")
            return 0
        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при извлечении числа: {e}")
            raise

    @allure.step("Кликнуть на кнопку закрытия (крестик)")
    def click_close_button(self):
        """Закрыть модальное окно кликом по крестику"""
        try:
            # Пробуем найти и кликнуть на кнопку закрытия
            if self.is_element_visible(self.locators.CLOSE_BUTTON, timeout=3):
                self.click_element(self.locators.CLOSE_BUTTON)
                return True

            # Если кнопка не найдена, пробуем альтернативные селекторы
            alternative_selectors = [
                (By.CSS_SELECTOR, "button[class*='close']"),
                (By.CSS_SELECTOR, "svg[class*='close']"),
                (By.XPATH, "//button[contains(@aria-label, 'закрыть') or contains(@aria-label, 'close')]"),
            ]

            for selector in alternative_selectors:
                try:
                    elements = self.find_elements(selector, timeout=1)
                    for element in elements:
                        if element.is_displayed() and element.is_enabled():
                            element.click()
                            return True
                except (TimeoutException, NoSuchElementException):
                    continue
                except (ElementNotInteractableException, StaleElementReferenceException) as e:
                    self.logger.warning(f"Элемент не доступен для взаимодействия: {e}")
                    continue

            self.logger.warning("Не удалось найти кнопку закрытия модального окна")
            return False

        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при клике на кнопку закрытия: {e}")
            raise

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        """Закрыть модальное окно с ожиданием"""
        try:
            # Проверяем, открыто ли окно
            if not self.is_modal_opened():
                self.logger.info("Модальное окно уже закрыто")
                return True

            # Закрываем окно
            success = self.click_close_button()

            if not success:
                # Пробуем кликнуть по оверлею
                if self.is_element_visible(self.locators.MODAL_OVERLAY, timeout=2):
                    try:
                        overlay = self.find_element(self.locators.MODAL_OVERLAY)
                        overlay.click()
                        success = True
                    except (ElementNotInteractableException, ElementNotVisibleException) as e:
                        self.logger.warning(f"Оверлей не доступен для клика: {e}")

                # Если всё еще не получилось, используем Escape
                if not success:
                    try:
                        actions = self.create_action_chains()
                        actions.send_keys(Keys.ESCAPE).perform()
                        success = True
                    except Exception as e:
                        self.logger.warning(f"Не удалось закрыть модальное окно через Escape: {e}")

            # Ожидаем закрытия окна
            if success:
                try:
                    return self.wait_for_modal_close(timeout=5)
                except TimeoutException:
                    self.logger.warning("Модальное окно не закрылось после попытки закрытия")
                    return False

            return False

        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при закрытии модального окна: {e}")
            raise

    @allure.step("Ожидать открытия модального окна")
    def wait_for_modal_open(self, timeout=10):
        """Ожидать открытия модального окна"""
        try:
            return self.wait_for_element_visible(
                self.locators.MODAL_CONTAINER,
                timeout=timeout
            )
        except TimeoutException as e:
            self.logger.warning(f"Модальное окно не открылось за {timeout} секунд: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при ожидании открытия модального окна: {e}")
            raise

    @allure.step("Ожидать закрытия модального окна")
    def wait_for_modal_close(self, timeout=10):
        """Ожидать закрытия модального окна"""
        try:
            return self.wait_for_element_to_disappear(
                self.locators.MODAL_CONTAINER,
                timeout=timeout
            )
        except TimeoutException as e:
            self.logger.warning(f"Модальное окно не закрылось за {timeout} секунд: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Непредвиденная ошибка при ожидании закрытия модального окна: {e}")
            raise