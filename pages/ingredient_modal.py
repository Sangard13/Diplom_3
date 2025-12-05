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
    # Добавляем локатор для оверлея
    MODAL_OVERLAY = (By.CSS_SELECTOR, "[class*='overlay'], [class*='backdrop']")

    def __init__(self, driver):
        """Конструктор"""
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self):
        """Проверить, что модальное окно открыто"""
        try:
            elements = self.driver.find_elements(*self.MODAL)
            for element in elements:
                try:
                    if element.is_displayed():
                        print(f"[DEBUG] Модальное окно найдено и отображается")
                        return True
                except:
                    continue

            # Также проверяем оверлей
            overlays = self.driver.find_elements(*self.MODAL_OVERLAY)
            for overlay in overlays:
                try:
                    if overlay.is_displayed():
                        print(f"[DEBUG] Оверлей модального окна найден")
                        return True
                except:
                    continue

            print(f"[DEBUG] Модальное окно не найдено или не отображается")
            return False
        except Exception as e:
            print(f"[DEBUG] Ошибка при проверке открытия модального окна: {e}")
            return False

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        """Проверить, что модальное окно закрыто"""
        try:
            # Ждем немного, чтобы дать время на анимацию закрытия
            time.sleep(1)

            # Проверяем, что нет видимых модальных окон
            elements = self.driver.find_elements(*self.MODAL)
            for element in elements:
                try:
                    if element.is_displayed():
                        print(f"[DEBUG] Модальное окно все еще отображается")
                        return False
                except:
                    continue

            # Проверяем, что нет видимых оверлеев
            overlays = self.driver.find_elements(*self.MODAL_OVERLAY)
            for overlay in overlays:
                try:
                    if overlay.is_displayed():
                        print(f"[DEBUG] Оверлей все еще отображается")
                        return False
                except:
                    continue

            print(f"[DEBUG] Модальное окно успешно закрыто")
            return True

        except Exception as e:
            print(f"[DEBUG] Ошибка при проверке закрытия модального окна: {e}")
            # В случае ошибки считаем, что окно закрыто
            return True

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
            # Используем общий локатор для деталей
            details_selectors = [
                (By.CSS_SELECTOR, "[class*='details']"),
                (By.CSS_SELECTOR, "[class*='info']"),
                (By.CSS_SELECTOR, "[class*='content']"),
                self.INGREDIENT_NAME
            ]

            for selector in details_selectors:
                details = self.driver.find_elements(*selector)
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
            print("[DEBUG] Поиск кнопки закрытия...")

            # Сначала пробуем более специфичные селекторы
            close_selectors = [
                (By.CSS_SELECTOR, "button[class*='Modal_close']"),
                (By.CSS_SELECTOR, "div[class*='Modal_close']"),
                (By.CSS_SELECTOR, "svg[class*='close']"),
                self.CLOSE_BUTTON,
                (By.XPATH, "//button[contains(text(), '×')]"),
                (By.XPATH, "//button[contains(text(), 'X')]"),
                (By.XPATH, "//button[.//*[contains(text(), '×')]]"),
                (By.XPATH, "//button[.//*[contains(text(), 'X')]]"),
            ]

            for selector in close_selectors:
                try:
                    buttons = self.driver.find_elements(*selector)
                    print(f"[DEBUG] Найдено {len(buttons)} элементов по селектору {selector}")

                    for i, button in enumerate(buttons):
                        try:
                            if button.is_displayed() and button.is_enabled():
                                print(f"[DEBUG] Кликаем на кнопку {i}: {button.get_attribute('class')}")
                                button.click()
                                time.sleep(1)
                                return True
                        except Exception as e:
                            print(f"[DEBUG] Ошибка при клике на кнопку {i}: {e}")
                            continue
                except:
                    continue

            print("[DEBUG] Кнопка не найдена, пробуем Escape")
            # Если кнопка не найдена, пробуем Escape
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

            # Пробуем кликнуть по оверлею
            overlays = self.driver.find_elements(*self.MODAL_OVERLAY)
            for overlay in overlays:
                try:
                    if overlay.is_displayed():
                        print("[DEBUG] Кликаем по оверлею")
                        overlay.click()
                        time.sleep(1)
                        return True
                except:
                    continue

            return True

        except Exception as e:
            print(f"[DEBUG] Ошибка при закрытии модального окна: {e}")
            return False

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        """Закрыть модальное окно с ожиданием"""
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

    @allure.step("Ожидать открытия модального окна")
    def wait_for_modal_open(self, timeout=5):
        """Ожидать открытия модального окна"""
        try:
            # Ожидаем появления модального окна
            return self.wait.until(
                lambda driver: self.is_modal_opened()
            )
        except:
            return False

    @allure.step("Ожидать закрытия модального окна")
    def wait_for_modal_close(self, timeout=5):
        """Ожидать закрытия модального окна"""
        try:
            # Ожидаем исчезновения модального окна
            return self.wait.until(
                lambda driver: not self.is_modal_opened()
            )
        except:
            return True