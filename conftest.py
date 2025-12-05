import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

# Добавляем корневую директорию в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Импортируем конфигурацию из вашего файла
try:
    from config import BASE_URL, TEST_USER, TIMEOUTS

    DEFAULT_BASE_URL = BASE_URL
    DEFAULT_TEST_USER = TEST_USER
except ImportError:
    # Запасные значения, если config.py не найден
    DEFAULT_BASE_URL = "https://stellarburgers.education-services.ru"
    DEFAULT_TEST_USER = {
        'name': 'Vinnik',
        'email': 'qaefsf13@hmaul.com',
        'password': '123456789'
    }


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
        default=DEFAULT_BASE_URL,
        help="Базовый URL приложения"
    )
    parser.addoption(
        "--user-email",
        action="store",
        default=DEFAULT_TEST_USER['email'],
        help="Email тестового пользователя"
    )
    parser.addoption(
        "--user-password",
        action="store",
        default=DEFAULT_TEST_USER['password'],
        help="Пароль тестового пользователя"
    )


@pytest.fixture(scope="function")
def test_user(request):
    """Фикстура для получения тестового пользователя"""
    email = request.config.getoption("--user-email")
    password = request.config.getoption("--user-password")

    return {
        'name': DEFAULT_TEST_USER.get('name', 'Vinnik'),
        'email': email,
        'password': password
    }


@pytest.fixture(scope="function")
def authorized_user(driver, base_url, test_user):
    """Фикстура для авторизованного пользователя"""
    try:
        # Импортируем здесь, чтобы избежать циклических импортов
        from pages.login_page import LoginPage
        from pages.main_page import MainPage

        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        # Переходим на главную страницу
        main_page.open_main_page()

        # Проверяем, не авторизованы ли мы уже
        try:
            if hasattr(main_page, 'is_user_authorized') and main_page.is_user_authorized():
                print("Пользователь уже авторизован")
                return main_page
        except:
            pass

        # Если не авторизованы, выполняем авторизацию
        try:
            main_page.click_login_button()
        except Exception as e:
            print(f"Не удалось нажать кнопку логина: {e}")
            # Пробуем перейти на страницу логина напрямую
            driver.get(f"{base_url}/login")

        # Авторизация
        login_page.login(test_user['email'], test_user['password'])

        # Ожидаем успешной авторизации
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != f"{base_url}/login"
        )

        # Возвращаемся на главную страницу
        main_page.open_main_page()

        # Даем время для обновления состояния
        import time
        time.sleep(2)

        return main_page

    except Exception as e:
        print(f"Ошибка в authorized_user: {e}")
        # В случае ошибки все равно возвращаем main_page
        return main_page


@pytest.fixture
def browser(request):
    """Фикстура выбора браузера"""
    return request.config.getoption("--browser")


@pytest.fixture
def headless(request):
    """Фикстура headless режима"""
    return request.config.getoption("--headless")


@pytest.fixture
def base_url(request):
    """Базовый URL тестового приложения"""
    return request.config.getoption("--base-url")


@pytest.fixture
def driver(browser, headless, base_url):
    """Универсальная фикстура драйвера"""
    driver_instance = None

    print(f"\n🚀 Запуск теста в браузере: {browser}")
    print(f"   Headless режим: {'Да' if headless else 'Нет'}")
    print(f"   Base URL: {base_url}")

    try:
        if browser.lower() == "chrome":
            options = Options()

            if headless:
                options.add_argument("--headless=new")

            # Основные настройки
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--disable-notifications")
            options.add_argument("--lang=ru")

            # Отключение автоматизации
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            # Отключение предупреждений в консоли
            options.add_experimental_option('excludeSwitches', ['enable-logging'])

            # User agent
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

            driver_instance = webdriver.Chrome(options=options)

        else:
            raise ValueError(f"Браузер {browser} не поддерживается")

        # Общие настройки
        driver_instance.implicitly_wait(10)
        driver_instance.set_page_load_timeout(30)
        driver_instance.set_script_timeout(30)

        # Добавляем информацию в Allure отчет
        allure.dynamic.tag(browser)
        allure.dynamic.link(base_url, name="Тестируемое приложение")

    except Exception as e:
        print(f"❌ Ошибка при создании драйвера {browser}: {e}")
        raise e

    yield driver_instance

    print(f"\n🔚 Закрытие браузера: {browser}")
    driver_instance.quit()


# Фикстуры страниц
@pytest.fixture
def main_page(driver):
    """Главная страница"""
    from pages.main_page import MainPage
    page = MainPage(driver)
    return page


@pytest.fixture
def login_page(driver):
    """Страница логина"""
    from pages.login_page import LoginPage
    page = LoginPage(driver)
    return page


@pytest.fixture
def feed_page(driver):
    """Страница ленты заказов (алиас для order_feed_page)"""
    from pages.order_feed_page import OrderFeedPage
    page = OrderFeedPage(driver)
    return page

# Уберите дублирующую фикстуру order_feed_page или оставьте как алиас
@pytest.fixture
def order_feed_page(driver):
    """Страница ленты заказов"""
    from pages.order_feed_page import OrderFeedPage
    page = OrderFeedPage(driver)
    return page

@pytest.fixture
def profile_page(driver):
    """Страница профиля"""
    from pages.profile_page import ProfilePage
    page = ProfilePage(driver)
    return page

@pytest.fixture
def ingredient_modal(driver):
    """Модальное окно ингредиента"""
    from pages.ingredient_modal import IngredientModal  # <- ваш класс
    return IngredientModal(driver)


# Хук для создания скриншотов при падении тестов
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Создание скриншотов при падении тестов"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Получаем драйвер из фикстур
        for fixture_name in item.fixturenames:
            if "driver" in fixture_name:
                driver_fixture = item.funcargs.get(fixture_name)
                if driver_fixture:
                    try:
                        # Скриншот
                        screenshot = driver_fixture.get_screenshot_as_png()
                        allure.attach(
                            screenshot,
                            name="screenshot_on_failure",
                            attachment_type=allure.attachment_type.PNG
                        )

                        # Текущий URL
                        url = driver_fixture.current_url
                        allure.attach(
                            url,
                            name="current_url",
                            attachment_type=allure.attachment_type.TEXT
                        )

                        # Исходный код страницы
                        page_source = driver_fixture.page_source[:5000]  # Первые 5000 символов
                        allure.attach(
                            page_source,
                            name="page_source",
                            attachment_type=allure.attachment_type.TEXT
                        )
                    except Exception as e:
                        print(f"Не удалось сделать скриншот: {e}")
                break


# Фикстура для Faker (если нужно)
@pytest.fixture(scope="session")
def faker():
    """Фикстура для генерации тестовых данных"""
    try:
        from faker import Faker
        return Faker('ru_RU')
    except ImportError:
        return None


# Фикстура для временного ожидания
@pytest.fixture
def wait():
    """Фикстура для явных ожиданий"""

    def custom_wait(seconds):
        import time
        time.sleep(seconds)

    return custom_wait