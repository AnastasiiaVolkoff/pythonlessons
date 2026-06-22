from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    # Шаг 1: найти все ссылки (<a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # Шаг 2: проверить количество (должно быть 9)
    assert len(links) == 9

    # Шаг 3: проверить, что все ссылки отображаются
    for link in links:
        assert link.is_displayed()

    # Шаг 4: проверить, что текст первой ссылки содержит "1"
    assert "1" in links[0].text

    driver.quit()
