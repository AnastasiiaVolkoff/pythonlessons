"""
Модуль с Page Object для страницы калькулятора.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object для страницы калькулятора.
    Содержит методы для взаимодействия с элементами калькулятора.
    """

    def __init__(self, driver):
        """
        Инициализация Page Object.

        Args:
            driver: WebDriver экземпляр для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Открывает страницу калькулятора.

        Returns:
            CalculatorPage: Возвращает текущий объект для цепочки методов.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds: int):
        """
        Устанавливает задержку перед вычислением.

        Args:
            seconds: Количество секунд задержки.

        Returns:
            CalculatorPage: Возвращает текущий объект для цепочки методов.
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, text: str):
        """
        Нажимает кнопку калькулятора по тексту.

        Args:
            text: Текст на кнопке (например, "7", "+", "=").

        Returns:
            CalculatorPage: Возвращает текущий объект для цепочки методов.
        """
        btn = self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        )
        btn.click()
        return self

    def get_result(self, expected_result: str, timeout: int = 50) -> str:
        """
        Ожидает появления результата и возвращает его.

        Args:
            expected_result: Ожидаемое значение результата.
            timeout: Максимальное время ожидания в секундах.

        Returns:
            str: Текст результата на экране калькулятора.
        """
        self.wait = WebDriverWait(self.driver, timeout)
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected_result
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
