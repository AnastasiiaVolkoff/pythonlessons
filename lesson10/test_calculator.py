"""
Тесты для калькулятора с использованием Page Object и Allure.
"""
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Проверка арифметических операций")
@allure.title("Проверка сложения с задержкой 45 секунд")
@allure.description(
    "Тест проверяет, что калькулятор корректно выполняет сложение "
    "7 + 8 = 15 с задержкой 45 секунд."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    with allure.step("Настройка браузера Chrome"):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

    try:
        with allure.step("Открытие страницы калькулятора и настройка задержки"):
            calc_page = CalculatorPage(driver)
            calc_page.open().set_delay(45)

        with allure.step("Ввод выражения 7 + 8 ="):
            calc_page.click_button("7") \
                    .click_button("+") \
                    .click_button("8") \
                    .click_button("=")

        with allure.step("Ожидание и проверка результата"):
            result = calc_page.get_result("15", timeout=50)
            assert result == "15", f"Ожидалось 15, получено {result}"
            allure.attach(
                f"Результат: {result}",
                name="Результат вычисления",
                attachment_type=allure.attachment_type.TEXT
            )

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
