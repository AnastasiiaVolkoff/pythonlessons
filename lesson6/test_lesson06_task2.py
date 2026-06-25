from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    # ------------------------------------------------------------
    # 1. Установить cookie для пользователя 1
    # ------------------------------------------------------------
    cookies_user1 = [
        {"name": "sessionid",
         "value": ("3:1777287789.5.0.1772320208248:pYNCsg:385e.1.2:1|"
                   "1130000069222383.-1.20000.2:4967581.3:1777287789|"
                   "3:11866677.224111.9LxLmDgY9L5Bj-MlL41FXRtyldI")},
        {"name": "csrftoken", "value": "7f919199-a7cb-4ee4-8ffc-b32681533ea1"},
    ]
    for cookie in cookies_user1:
        driver.add_cookie(cookie)

    driver.refresh()

    # 2. Перейти на страницу пользователя 1
    profile_url_1 = "https://gitflic.ru/user/melmalone"
    driver.get(profile_url_1)

    # Явное ожидание: дождаться, когда в URL появится /user/
    WebDriverWait(driver, 10).until(
        EC.url_contains("/user/")
    )

    url_user1 = driver.current_url
    print(f"URL пользователя 1: {url_user1}")

    # 3. Разлогиниться (очистить cookies)
    driver.delete_all_cookies()
    driver.refresh()

    # ------------------------------------------------------------
    # 4. Установить cookie для пользователя 2
    # ------------------------------------------------------------
    cookies_user2 = [
        {"name": "sessionid",
         "value": ("3:1782060051.5.0.1768832608296:sZ1Csg:ebbe.1.2:1|"
                   "783475754.0.2.3:1768832608.6:2216283090.7:1768832608|"
                   "3:11988850.909710.OLrcGvXA0beQA2cGizu7BWppse8")},
        {"name": "csrftoken", "value": "7f919199-a7cb-4ee4-8ffc-b32681533ea1"},
    ]
    for cookie in cookies_user2:
        driver.add_cookie(cookie)

    driver.refresh()

    # 5. Перейти на страницу пользователя 2
    profile_url_2 = "https://gitflic.ru/user/reginaprincess24"
    driver.get(profile_url_2)

    WebDriverWait(driver, 10).until(
        EC.url_contains("/user/")
    )

    url_user2 = driver.current_url
    print(f"URL пользователя 2: {url_user2}")

    # 6. Проверить, что URL различаются
    assert url_user1 != url_user2, "URL пользователей должны различаться!"

    driver.quit()
