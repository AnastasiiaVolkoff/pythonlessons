"""
Тесты для интернет-магазина с использованием Page Object и Allure.
"""
import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from shop_pages import LoginPage


@allure.feature("Интернет-магазин")
@allure.story("Оформление заказа")
@allure.title("Проверка оформления заказа стандартным пользователем")
@allure.description(
    "Тест проверяет, что стандартный пользователь может добавить "
    "3 товара в корзину и оформить заказ с итоговой суммой $58.29."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    """
    Тест магазина:
    1. Авторизация
    2. Добавление 3 товаров в корзину
    3. Переход в корзину и оформление заказа
    4. Проверка итоговой суммы
    """
    with allure.step("Настройка браузера Chrome"):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "autofill.profile_enabled": False,
            }
        )

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

    try:
        with allure.step("Авторизация как standard_user"):
            login_page = LoginPage(driver)
            inventory_page = login_page.open().login(
                "standard_user", "secret_sauce"
            )
            time.sleep(1)  # небольшая пауза

        with allure.step("Добавление 3 товаров в корзину"):
            inventory_page.add_to_cart("Sauce Labs Backpack") \
                          .add_to_cart("Sauce Labs Bolt T-Shirt") \
                          .add_to_cart("Sauce Labs Onesie")
            time.sleep(1)  # пауза после добавления

        with allure.step("Переход в корзину и оформление заказа"):
            cart_page = inventory_page.go_to_cart()
            checkout_page = cart_page.proceed_to_checkout()
            checkout_page.fill_form("Иван", "Петров", "123456")
            time.sleep(1)  # пауза перед проверкой

        with allure.step("Проверка итоговой суммы"):
            total_text = checkout_page.get_total()
            assert "$58.29" in total_text, (
                f"Итоговая сумма не $58.29, а {total_text}"
            )
            allure.attach(
                total_text,
                name="Итоговая сумма",
                attachment_type=allure.attachment_type.TEXT
            )

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
