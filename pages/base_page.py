import allure
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    # ========== Базовые методы для работы с элементами ==========

    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        """Найти элемент по локатору"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException as e:
            self.logger.error(f"Элемент не найден: {locator}, ошибка: {e}")
            raise

    @allure.step("Найти элементы")
    def find_elements(self, locator, timeout=10):
        """Найти все элементы по локатору"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException as e:
            self.logger.error(f"Элементы не найдены: {locator}, ошибка: {e}")
            return []

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=10):
        """Кликнуть на элемент"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            return True
        except Exception as e:
            self.logger.error(f"Не удалось кликнуть на элемент: {locator}, ошибка: {e}")
            return False

    @allure.step("Ввести текст в поле")
    def enter_text(self, locator, text, timeout=10):
        """Ввести текст в поле"""
        try:
            element = self.wait_for_element_visible(locator, timeout)
            element.clear()
            element.send_keys(text)
            return True
        except Exception as e:
            self.logger.error(f"Не удалось ввести текст: {locator}, ошибка: {e}")
            return False

    @allure.step("Получить текст элемента")
    def get_text(self, locator, timeout=10):
        """Получить текст элемента"""
        try:
            element = self.wait_for_element_visible(locator, timeout)
            return element.text.strip()
        except Exception as e:
            self.logger.error(f"Не удалось получить текст: {locator}, ошибка: {e}")
            return ""

    # ========== Методы ожидания ==========

    @allure.step("Ожидать видимости элемента")
    def wait_for_element_visible(self, locator, timeout=10):
        """Ждать, пока элемент станет видимым"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException as e:
            self.logger.error(f"Элемент не стал видимым: {locator}, ошибка: {e}")
            raise

    @allure.step("Ожидать присутствия элемента")
    def wait_for_element_present(self, locator, timeout=10):
        """Ждать присутствия элемента в DOM"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException as e:
            self.logger.error(f"Элемент не найден в DOM: {locator}, ошибка: {e}")
            raise

    @allure.step("Ожидать кликабельности элемента")
    def wait_for_element_clickable(self, locator, timeout=10):
        """Ждать, пока элемент станет кликабельным"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException as e:
            self.logger.error(f"Элемент не стал кликабельным: {locator}, ошибка: {e}")
            raise

    @allure.step("Ожидать исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Ждать, пока элемент не исчезнет"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    @allure.step("Ожидать устаревания элемента")
    def wait_for_element_staleness(self, element, timeout=10):
        """Ждать, пока элемент не станет устаревшим"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.staleness_of(element)
            )
        except TimeoutException as e:
            self.logger.error(f"Элемент не стал устаревшим, ошибка: {e}")
            return False

    @allure.step("Ожидать появления нескольких элементов")
    def wait_for_elements_present(self, locator, timeout=10, min_count=1):
        """Ждать появления хотя бы N элементов"""
        try:
            def elements_present(driver):
                elements = driver.find_elements(*locator)
                return len(elements) >= min_count

            WebDriverWait(self.driver, timeout).until(elements_present)
            return self.driver.find_elements(*locator)
        except TimeoutException as e:
            self.logger.error(f"Элементы не появились: {locator}, ошибка: {e}")
            return []

    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        """Ждать полной загрузки страницы"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )
            return True
        except TimeoutException as e:
            self.logger.error(f"Страница не загрузилась, ошибка: {e}")
            return False

    @allure.step("Ожидать, что URL содержит текст")
    def wait_for_url_contains(self, text, timeout=10):
        """Ждать, что URL содержит определенный текст"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException as e:
            self.logger.error(f"URL не содержит текст '{text}', ошибка: {e}")
            return False

    @allure.step("Ожидать выполнения условия")
    def wait_for_condition(self, condition_function, timeout=10):
        """Ждать выполнения пользовательского условия"""
        try:
            WebDriverWait(self.driver, timeout).until(condition_function)
            return True
        except TimeoutException as e:
            self.logger.error(f"Условие не выполнено, ошибка: {e}")
            return False

    # ========== Методы проверки ==========

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator, timeout=5):
        """Проверить, виден ли элемент"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить присутствие элемента")
    def is_element_present(self, locator, timeout=5):
        """Проверить, присутствует ли элемент в DOM"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить кликабельность элемента")
    def is_element_clickable(self, locator, timeout=5):
        """Проверить, кликабелен ли элемент"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False

    # ========== Методы взаимодействия ==========

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        """Перетащить элемент из source в target"""
        try:
            source = self.wait_for_element_visible(source_locator)
            target = self.wait_for_element_visible(target_locator)

            actions = ActionChains(self.driver)
            actions.drag_and_drop(source, target).perform()
            return True
        except Exception as e:
            self.logger.error(f"Ошибка при перетаскивании: {e}")
            return False

    @allure.step("Перетащить конкретный элемент")
    def drag_and_drop_element(self, source_element, target_element):
        """Перетащить элемент из source в target"""
        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source_element, target_element).perform()
            return True
        except Exception as e:
            self.logger.error(f"Ошибка при перетаскивании элемента: {e}")
            return False

    @allure.step("Создать цепочку действий")
    def create_action_chains(self):
        """Создать объект ActionChains"""
        return ActionChains(self.driver)

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        """Выполнить JavaScript"""
        try:
            return self.driver.execute_script(script, *args)
        except Exception as e:
            self.logger.error(f"Ошибка при выполнении JavaScript: {e}")
            return None

    @allure.step("Перетащить с помощью JavaScript")
    def drag_and_drop_js(self, source_locator, target_locator):
        """Перетащить элемент с помощью JavaScript"""
        try:
            source = self.find_element(source_locator)
            target = self.find_element(target_locator)

            script = """
            var source = arguments[0];
            var target = arguments[1];
            var event = new MouseEvent('dragstart', { bubbles: true });
            source.dispatchEvent(event);
            event = new MouseEvent('dragenter', { bubbles: true });
            target.dispatchEvent(event);
            event = new MouseEvent('dragover', { bubbles: true });
            target.dispatchEvent(event);
            event = new MouseEvent('drop', { bubbles: true });
            target.dispatchEvent(event);
            event = new MouseEvent('dragend', { bubbles: true });
            source.dispatchEvent(event);
            """

            self.execute_script(script, source, target)
            return True
        except Exception as e:
            self.logger.error(f"Ошибка при перетаскивании через JS: {e}")
            return False

    # ========== Методы навигации ==========

    @allure.step("Открыть URL")
    def open(self, url):
        """Открыть URL"""
        self.driver.get(url)
        self.wait_for_page_load()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL страницы"""
        return self.driver.current_url

    @allure.step("Обновить страницу")
    def refresh_page(self):
        """Обновить текущую страницу"""
        self.driver.refresh()
        self.wait_for_page_load()

    # ========== Вспомогательные методы ==========

    @allure.step("Найти элементы внутри родительского элемента")
    def find_elements_within_element(self, parent_element, locator):
        """Найти элементы внутри родительского элемента"""
        try:
            return parent_element.find_elements(*locator)
        except Exception as e:
            self.logger.error(f"Ошибка при поиске элементов внутри родителя: {e}")
            return []

    @allure.step("Сделать скриншот")
    def take_screenshot(self, name="screenshot"):
        """Сделать скриншот"""
        try:
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
            return True
        except Exception as e:
            self.logger.error(f"Ошибка при создании скриншота: {e}")
            return False

    @allure.step("Ожидать готовности документа")
    def wait_for_document_ready(self, timeout=10):
        """Ждать полной готовности DOM"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )
            return True
        except TimeoutException as e:
            self.logger.error(f"Документ не загрузился, ошибка: {e}")
            return False

    @allure.step("Ожидать текста в исходном коде страницы")
    def wait_for_text_in_page_source(self, keywords, min_matches=1, timeout=10):
        """Ждать появления текста в исходном коде страницы"""
        if isinstance(keywords, str):
            keywords = [keywords]

        def page_contains_keywords(driver):
            page_source = driver.page_source.lower()
            matches = sum(1 for kw in keywords if kw.lower() in page_source)
            return matches >= min_matches

        try:
            WebDriverWait(self.driver, timeout).until(page_contains_keywords)
            return True
        except TimeoutException as e:
            self.logger.error(f"Текст не найден на странице: {keywords}, ошибка: {e}")
            return False