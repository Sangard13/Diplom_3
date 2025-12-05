import allure
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IngredientModal(BasePage):
    """Класс для работы с модальным окном деталей ингредиента"""

    # Упрощенные локаторы для отладки
    MODAL = (By.CSS_SELECTOR, "div[class*='Modal_modal'], div[class*='modal'], [role='dialog']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='close'], svg[class*='close'], div[class*='close']")
    MODAL_TITLE = (By.CSS_SELECTOR, "h1, h2, h3, [class*='title']")
    INGREDIENT_NAME = (By.CSS_SELECTOR, "[class*='name'], [class*='title']")

    def __init__(self, driver):
        """Конструктор"""
        super().__init__(driver)

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self):
        """Проверить, что модальное окно открыто"""
        try:
            elements = self.driver.find_elements(*self.MODAL)
            for element in elements:
                try:
                    if element.is_displayed():
                        return True
                except:
                    continue
            return False
        except:
            return False

    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        """Получить текст заголовка модального окна"""
        try:
            titles = self.driver.find_elements(*self.MODAL_TITLE)
            for title in titles:
                try:
                    if title.is_displayed() and title.text.strip():
                        return title.text.strip()
                except:
                    continue
            return "Заголовок не найден"
        except:
            return ""

    @allure.step("Проверить наличие деталей ингредиента")
    def is_ingredient_details_visible(self):
        """Проверить, отображаются ли детали ингредиента"""
        try:
            details = self.driver.find_elements(*self.INGREDIENT_DETAILS)
            for detail in details:
                try:
                    if detail.is_displayed():
                        return True
                except:
                    continue
            return False
        except:
            return False

    @allure.step("Кликнуть на кнопку закрытия (крестик)")
    def click_close_button(self):
        """Закрыть модальное окно кликом по крестику"""
        try:
            close_buttons = self.driver.find_elements(*self.CLOSE_BUTTON)
            for button in close_buttons:
                try:
                    if button.is_displayed():
                        button.click()
                        time.sleep(1)
                        return True
                except:
                    continue

            # Если кнопка не найдена, пробуем Escape
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            return True

        except Exception as e:
            print(f"[DEBUG] Ошибка при закрытии модального окна: {e}")
            return False

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        """Закрыть модальное окно с ожиданием"""
        import time

        print("[DEBUG] Начало закрытия модального окна")

        # Проверяем, открыто ли окно
        if not self.is_modal_opened():
            print("[DEBUG] Модальное окно уже закрыто")
            return True

        # Закрываем окно
        self.click_close_button()

        # Ждем закрытия (до 5 секунд)
        for i in range(10):
            time.sleep(0.5)
            if not self.is_modal_opened():
                print(f"[DEBUG] Модальное окно закрылось после {i + 1} попытки")
                return True

        print("[DEBUG] Модальное окно не закрылось после всех попыток")
        return False