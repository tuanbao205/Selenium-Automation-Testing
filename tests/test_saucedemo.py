"""UI automation tests for the public SauceDemo demo website."""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.saucedemo.com/"
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    """Start a fresh Chrome browser for each test and always close it."""
    options = webdriver.ChromeOptions()
    # Keep the browser visible so test execution can be demonstrated.
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1366, 900)
    browser.implicitly_wait(0)
    yield browser
    browser.quit()


def wait_for(driver, condition, timeout=10):
    """Wait until a Selenium expected condition is satisfied."""
    return WebDriverWait(driver, timeout).until(condition)


def login(driver, username=VALID_USERNAME, password=VALID_PASSWORD):
    driver.get(BASE_URL)
    wait_for(driver, EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def test_valid_login_opens_products_page(driver):
    """TC01: Valid credentials should open the inventory page."""
    login(driver)
    wait_for(driver, EC.url_contains("inventory.html"))
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"


def test_invalid_password_shows_error(driver):
    """TC02: An invalid password should show a login error."""
    login(driver, password="wrong_password")
    error = wait_for(
        driver,
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")),
    )
    assert "Username and password do not match" in error.text


def test_products_are_displayed(driver):
    """TC03: The products page should contain visible inventory items."""
    login(driver)
    wait_for(driver, EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    assert len(products) > 0


def test_adding_product_updates_cart_badge(driver):
    """TC04: Adding a product should set the cart badge to one."""
    login(driver)
    wait_for(
        driver,
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")),
    ).click()
    badge = wait_for(
        driver,
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")),
    )
    assert badge.text == "1"


def test_removing_product_empties_cart(driver):
    """TC05: Removing the only cart item should empty the cart."""
    login(driver)
    wait_for(
        driver,
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")),
    ).click()

    wait_for(
        driver,
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")),
    ).click()
    wait_for(driver, EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))

    wait_for(
        driver,
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack")),
    ).click()

    wait_for(driver, EC.invisibility_of_element_located((By.CLASS_NAME, "cart_item")))
    assert driver.find_elements(By.CLASS_NAME, "cart_item") == []
    assert driver.find_elements(By.CLASS_NAME, "shopping_cart_badge") == []
