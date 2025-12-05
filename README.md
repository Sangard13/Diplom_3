# Diplom_3

Проект автоматизации тестирования веб-приложения Stellar Burgers

# Основные зависимости:
```txt
pytest==7.4.0            # Фреймворк для тестирования
selenium==4.15.0         # Автоматизация браузера
allure-pytest==2.13.2    # Генерация отчетов Allure
webdriver-manager==4.0.1 # Автоматическое управление драйверами
Faker==20.1.0            # Генерация тестовых данных

# Дополнительные библиотеки:

pytest-xdist==3.5.0      # Параллельный запуск тестов
pytest-ordering==0.6.0   # Управление порядком выполнения тестов
Тесты ленты заказов (test_order_feed_functionality.py)

# Тесты основной функциональности приложения
(TestMainFunctionality)

test_navigate_to_constructor - Проверка перехода в раздел "Конструктор"
test_navigate_to_order_feed - Проверка навигации в раздел "Лента заказов"
test_click_ingredient_opens_modal - Проверка отображения деталей ингредиента
test_close_ingredient_modal_with_x - Проверка закрытия модального окна
test_ingredient_counter_increases - Проверка счетчика добавленных ингредиентов


# Тесты ленты заказов:

test_total_counter_displayed - Проверка отображения счётчика "Выполнено заказов
за всё время
test_today_counter_displayed - Проверка отображения дневного счетчика заказов
test_orders_in_progress_displayed - Проверка раздела "В работе"

# Используемые технологии:

Selenium WebDriver - автоматизация браузера
Allure Framework - генерация отчетов
Pytest - фреймворк для тестирования
Page Object Pattern - структурирование тестов

# Браузеры: Google Chrome, Mozilla Firefox

# Установка зависимостей:

pip install -r requirements.txt
Запуск всех тестов:
# Запуск в обоих браузерах
pytest --browser=chrome --browser=firefox -v
# Запуск с отчетом Allure
pytest --alluredir=allure-results --browser=chrome -v