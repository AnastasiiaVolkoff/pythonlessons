from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_form_validation():
    edge_options = Options()
    edge_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "autofill.profile_enabled": False,
            "profile.default_content_setting_values.notifications": 2
        }
    )
    edge_options.add_argument("--inprivate")
    edge_options.add_argument("--disable-notifications")
    edge_options.add_argument(
        "--disable-features=PasswordImport,PasswordExport,PasswordManager"
    )

    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=edge_options
    )
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    fields_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in fields_data.items():
        field = driver.find_element(By.NAME, name)
        field.clear()
        field.send_keys(value)

    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_btn.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("data-types-submitted.html"))
    assert "data-types-submitted.html" in driver.current_url

    driver.quit()
