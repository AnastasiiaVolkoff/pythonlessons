"""
Модуль с Page Object для интернет-магазина.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Страница авторизации."""

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        Args:
            driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Открывает страницу авторизации.

        Returns:
            LoginPage: Возвращает текущий объект.
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username: str, password: str):
        """
        Выполняет вход в систему.

        Args:
            username: Имя пользователя.
            password: Пароль.

        Returns:
            InventoryPage: Страница с товарами.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return InventoryPage(self.driver)


class InventoryPage:
    """Страница с товарами."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, item_name: str):
        """
        Добавляет товар в корзину по его названию.

        Args:
            item_name: Название товара.

        Returns:
            InventoryPage: Возвращает текущий объект.
        """
        item_xpath = (
            f"//div[text()='{item_name}']/ancestor::div["
            f"@class='inventory_item']//button"
        )
        self.driver.find_element(By.XPATH, item_xpath).click()
        return self

    def go_to_cart(self):
        """
        Переходит в корзину.

        Returns:
            CartPage: Страница корзины.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return CartPage(self.driver)


class CartPage:
    """Страница корзины."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def proceed_to_checkout(self):
        """
        Переходит к оформлению заказа.

        Returns:
            CheckoutPage: Страница оформления заказа.
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
        return CheckoutPage(self.driver)


class CheckoutPage:
    """Страница оформления заказа."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполняет форму заказа.

        Args:
            first_name: Имя.
            last_name: Фамилия.
            postal_code: Почтовый индекс.

        Returns:
            CheckoutPage: Возвращает текущий объект.
        """
        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total(self) -> str:
        """
        Получает итоговую стоимость заказа.

        Returns:
            str: Текст итоговой стоимости (например, "Total: $58.29").
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_element.text
