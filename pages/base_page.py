import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    """Базовый класс для всех Page Object классов"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть URL: {url}")
    def open(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    @allure.step("Найти элемент с локатором: {locator}")
    def find_element(self, locator, timeout=10):
        """Найти элемент с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти все элементы с локатором: {locator}")
    def find_elements(self, locator, timeout=10):
        """Найти все элементы с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator, timeout=10):
        """Кликнуть по элементу с ожиданием"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Ввести текст '{text}' в поле")
    def input_text(self, locator, text, timeout=10):
        """Ввести текст в поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator, timeout=10):
        """Получить текст элемента"""
        element = self.find_element(locator, timeout)
        return element.text.strip()

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator, timeout=10):
        """Проверить видимость элемента"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    @allure.step("Проверить наличие элемента")
    def is_element_present(self, locator, timeout=3):
        """Проверить наличие элемента на странице"""
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False

    @allure.step("Ждать исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Ждать исчезновения элемента"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    @allure.step("Ждать, что URL содержит текст: {text}")
    def wait_for_url_contains(self, text, timeout=10):
        """Ждать, что URL содержит определенный текст"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_contains(text))

    @allure.step("Drag and drop через ActionChains")
    def drag_and_drop(self, source_locator, target_locator):
        """Перетащить элемент с использованием ActionChains"""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step("Drag and drop через JavaScript")
    def drag_and_drop_js(self, source_locator, target_locator):
        """Перетащить элемент с использованием JavaScript"""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        js_script = """
        function simulateDragDrop(sourceNode, destinationNode) {
            var EVENT_TYPES = {
                DRAG_END: 'dragend',
                DRAG_START: 'dragstart',
                DROP: 'drop'
            }

            function createCustomEvent(type) {
                var event = new CustomEvent("CustomEvent")
                event.initCustomEvent(type, true, true, null)
                event.dataTransfer = {
                    data: {},
                    setData: function(type, val) {
                        this.data[type] = val
                    },
                    getData: function(type) {
                        return this.data[type]
                    }
                }
                return event
            }

            function dispatchEvent(node, type, event) {
                if (node.dispatchEvent) {
                    return node.dispatchEvent(event)
                }
                if (node.fireEvent) {
                    return node.fireEvent("on" + type, event)
                }
            }

            var event = createCustomEvent(EVENT_TYPES.DRAG_START)
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event)

            var dropEvent = createCustomEvent(EVENT_TYPES.DROP)
            dropEvent.dataTransfer = event.dataTransfer
            dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent)

            var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
            dragEndEvent.dataTransfer = event.dataTransfer
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent)
        }

        simulateDragDrop(arguments[0], arguments[1]);
        """

        self.driver.execute_script(js_script, source, target)

    @allure.step("Ожидать появления текста в элементе")
    def wait_for_text_in_element(self, locator, text, timeout=10):
        """Ожидать появления определенного текста в элементе"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Ожидать выполнения условия")
    def wait_for_custom_condition(self, condition, timeout=10):
        """Ожидать выполнения кастомного условия"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(condition)

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        """Выполнить JavaScript код"""
        return self.driver.execute_script(script, *args)


    @allure.step("Найти элемент (старый формат)")
    def find_element_by(self, by, value, timeout=10):
        """Найти элемент по by и value"""
        return self.find_element((by, value), timeout)

    @allure.step("Найти все элементы (старый формат)")
    def find_elements_by(self, by, value, timeout=10):
        """Найти все элементы по by и value"""
        return self.find_elements((by, value), timeout)

    @allure.step("Кликнуть по элементу (старый формат)")
    def click_element_by(self, by, value, timeout=10):
        """Кликнуть по элементу по by и value"""
        return self.click_element((by, value), timeout)

    @allure.step("Получить текст элемента (старый формат)")
    def get_element_text(self, by, value, timeout=10):
        """Получить текст элемента по by и value"""
        element = self.find_element((by, value), timeout)
        return element.text.strip()

    @allure.step("Проверить видимость элемента (старый формат)")
    def is_element_visible_by(self, by, value, timeout=10):
        """Проверить видимость элемента по by и value"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located((by, value)))
            return element.is_displayed()
        except:
            return False

    @allure.step("Получить атрибут элемента")
    def get_attribute(self, locator, attribute_name, timeout=10):
        """Получить значение атрибута элемента"""
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute_name)

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_ready_state(self, timeout=10):
        """Дождаться полной загрузки страницы"""

        def page_is_loaded(driver):
            return driver.execute_script("return document.readyState") == "complete"

        wait = WebDriverWait(self.driver, timeout)
        return wait.until(page_is_loaded)

    @allure.step("Сделать скриншот")
    def take_screenshot(self, filename="screenshot.png"):
        """Сделать скриншот текущей страницы"""
        self.driver.save_screenshot(filename)
        return filename

    @allure.step("Переключиться на iframe")
    def switch_to_frame(self, locator, timeout=10):
        """Переключиться на iframe"""
        frame = self.find_element(locator, timeout)
        self.driver.switch_to.frame(frame)

    @allure.step("Вернуться из iframe")
    def switch_to_default_content(self):
        """Вернуться из iframe на основную страницу"""
        self.driver.switch_to.default_content()

    @allure.step("Навести курсор на элемент")
    def hover_over_element(self, locator, timeout=10):
        """Навести курсор на элемент"""
        element = self.find_element(locator, timeout)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step("Принять alert")
    def accept_alert(self, timeout=10):
        """Принять alert"""
        wait = WebDriverWait(self.driver, timeout)
        alert = wait.until(EC.alert_is_present())
        alert.accept()

    @allure.step("Отклонить alert")
    def dismiss_alert(self, timeout=10):
        """Отклонить alert"""
        wait = WebDriverWait(self.driver, timeout)
        alert = wait.until(EC.alert_is_present())
        alert.dismiss()