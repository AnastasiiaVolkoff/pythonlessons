from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    # Шаг 1: найти поле ввода по атрибуту name="custname"
    name_field = driver.find_element(By.NAME, "custname")
    # Шаг 2: ввести имя
    name_field.send_keys("Анастасия")

    # Шаг 3: найти кнопку Submit по тексту (используем XPath)
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    # Шаг 4: проверить, что URL изменился (стал содержать /post)
    assert "/post" in driver.current_url

    driver.quit()
