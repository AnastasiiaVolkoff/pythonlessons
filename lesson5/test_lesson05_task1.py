from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    # Шаг 1: открыть главную страницу
    driver.get("https://httpbin.org/")
    main_url = driver.current_url

    # Шаг 2: найти и кликнуть по ссылке "HTML Form"
    link = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@href="/forms/post"]')
            ))
    link.click()

    # Шаг 3: проверить, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url

    # Шаг 4: вернуться назад
    driver.back()

    # Шаг 5: проверить, что вернулись на главную
    assert driver.current_url == main_url

    driver.quit()
