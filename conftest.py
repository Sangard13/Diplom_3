import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    """Добавление кастомных опций для запуска тестов"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для тестов: chrome или firefox"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless режиме"
    )
    parser.addoption(
        "--base-url",
        action="store",
        default="https://stellarburgers.education-services.ru",
        help="Базовый URL приложения"
    )


@pytest.fixture(scope="session")
def config(request):
    """Конфигурация тестового окружения"""
    return {
        "browser": request.config.getoption("--browser"),
        "headless": request.config.getoption("--headless"),
        "base_url": request.config.getoption("--base-url")
    }


@pytest.fixture(scope="function")
def driver(config):
    """Фикстура инициализации WebDriver"""
    browser = config["browser"].lower()
    headless = config["headless"]

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-tools")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # ← убираем логи

        driver_instance = webdriver.Chrome(options=options)

    elif browser in ["firefox", "mozilla"]:
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")

        driver_instance = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Браузер {browser} не поддерживается")

    driver_instance.implicitly_wait(5)

    allure.dynamic.tag(browser)
    allure.dynamic.link(config["base_url"], name="Тестируемое приложение")

    yield driver_instance

    driver_instance.quit()


@pytest.fixture(scope="function")
def base_url(config):
    """Базовый URL приложения"""
    return config["base_url"]


@pytest.fixture(scope="function")
def wait(driver):
    """Универсальный WebDriverWait для явных ожиданий"""
    return WebDriverWait(driver, timeout=10)


@pytest.fixture(scope="function")
def main_page(driver, base_url):
    """Главная страница"""
    from pages.main_page import MainPage
    page = MainPage(driver, base_url)
    page.open()
    return page


@pytest.fixture(scope="function")
def order_feed_page(driver, base_url):
    """Страница ленты заказов"""
    from pages.order_feed_page import OrderFeedPage
    page = OrderFeedPage(driver, base_url)
    page.open()
    return page

@pytest.fixture(scope="function")
def ingredient_modal(driver, base_url):
    """Модальное окно ингредиента"""
    from pages.ingredient_modal import IngredientModal
    return IngredientModal(driver, base_url)

@pytest.fixture(scope="function")
def login_page(driver, base_url):
    """Страница логина"""
    from pages.login_page import LoginPage
    page = LoginPage(driver, base_url)
    return page

@pytest.fixture
def login_page(driver, base_url):
    """Фикстура для страницы логина"""
    from pages.login_page import LoginPage
    page = LoginPage(driver, base_url)
    page.open()
    return page

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для сохранения результата выполнения теста"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture(scope="function")
def drag_and_drop_js():
    """
    JavaScript функция для drag-and-drop.
    Необходима для корректной работы в Firefox.
    """
    return """
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
                data: {
                },
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

@pytest.fixture
def feed_page(order_feed_page):
    """Алиас для order_feed_page"""
    return order_feed_page