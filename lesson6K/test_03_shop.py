from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


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
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items:
        add_button = driver.find_element(
            By.XPATH,
            f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"
        )
        add_button.click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text
    assert "58.29" in total_text, f"Итоговая сумма не $58.29, а {total_text}"

    driver.quit()
