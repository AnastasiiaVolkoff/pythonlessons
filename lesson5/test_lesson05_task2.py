from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_form_submission():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://httpbin.org/forms/post")

    # Шаг 1: найти поле ввода по атрибуту name="custname"
    name_field = wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "custname")
            ))
    # Шаг 2: ввести имя
    name_field.clear()
    name_field.send_keys("Анастасия")

    # Шаг 3: найти кнопку Submit по тексту (используем XPath)
    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button')
        ))
    submit_button.click()

    # Шаг 4: проверить, что URL изменился (стал содержать /post)
    assert "/post" in driver.current_url

    driver.quit()
