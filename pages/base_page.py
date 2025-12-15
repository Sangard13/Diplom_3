from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import allure

class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url


    def open(self):
        """Открыть страницу"""
        self.driver.get(self.url)

    def wait_for(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Найти элемент {locator} с ожиданием {timeout} секунд")
    def find_element(self, locator, timeout=10):
        """Найти элемент с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти несколько элементов {locator}")
    def find_elements(self, locator, timeout=10):
        """Найти несколько элементов с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=10):
        """Кликнуть по элементу"""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator, timeout=10):
        """Проверить, виден ли элемент с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    @allure.step("Перетащить элемент из {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        """Перетащить элемент"""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(source, target).perform()

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Ждет исчезновения элемента"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Заполнить поле {locator} текстом: {text}")
    def fill_field(self, locator, text):
        """Заполнить поле ввода"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator, timeout=10):
        """Кликнуть по элементу"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидать, что URL содержит текст: {text}")
    def wait_for_url_contains(self, text, timeout=10):
        """Ожидать, что URL содержит определенный текст"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_contains(text))

    @allure.step("Ожидать загрузки домашней страницы")
    def wait_for_home_page(self, timeout=10):
        """Ожидать загрузки домашней страницы"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_matches(r"^https?://[^/]+/?$"))

    def wait_for_element(self, locator, timeout=10):
        """Ожидать появления элемента"""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(self, locator, timeout=10):
        """Ожидать, что элемент станет видимым"""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_element_attribute(self, locator, attribute):
        """Получить атрибут элемента"""
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    def find_elements_by_text(self, text):
        """Найти элементы по тексту"""
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        return self.find_elements(locator)

    def find_elements_by_text_and_class(self, text, class_name):
        """Найти элементы по тексту и классу"""
        locator = (By.XPATH, f"//div[contains(@class, '{class_name}') and contains(text(), '{text}')]")
        return self.find_elements(locator)

    @allure.step("Обновить страницу")
    def refresh(self):
        """Обновить текущую страницу"""
        self.driver.refresh()