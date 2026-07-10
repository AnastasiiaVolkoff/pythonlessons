from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_calculator():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    calc_page = CalculatorPage(driver)

    calc_page.open() \
            .set_delay(45) \
            .click_button("7") \
            .click_button("+") \
            .click_button("8") \
            .click_button("=")

    result = calc_page.get_result("15", timeout=50)
    assert result == "15", f"Ожидалось 15, получено {result}"

    driver.quit()
