from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from shop_pages import LoginPage


def test_shop():
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

    login_page = LoginPage(driver)
    inventory_page = login_page.open().login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("Sauce Labs Backpack") \
                  .add_to_cart("Sauce Labs Bolt T-Shirt") \
                  .add_to_cart("Sauce Labs Onesie")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.fill_form("Иван", "Петров", "123456")

    total_text = checkout_page.get_total()
    assert "$58.29" in total_text, f"Итоговая сумма не $58.29, а {total_text}"

    driver.quit()
