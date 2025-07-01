import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from calculator_page import CalculatorPage 
import os
import sys

class TestCalculator:
    @pytest.fixture(scope="class")
    def driver(self):
        chrome_options = Options()
        if os.getenv('CI'):
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')

        path = ChromeDriverManager().install()
        if sys.platform.startswith("win") and not path.endswith("chromedriver.exe"):
            path = os.path.join(os.path.dirname(path), "chromedriver.exe")
        service = Service(path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_page_loads(self, driver):
        page = CalculatorPage(driver)
        page.load_page()

        assert "Calculatrice Simple" in driver.title
        assert driver.find_element(By.ID, "num1").is_displayed()
        assert driver.find_element(By.ID, "num2").is_displayed()
        assert driver.find_element(By.ID, "operation").is_displayed()
        assert driver.find_element(By.ID, "calculate").is_displayed()

    def test_addition(self, driver):
        page = CalculatorPage(driver)
        page.load_page()
        page.enter_first_number(10)
        page.enter_second_number(5)
        page.select_operation("add")
        page.click_calculate()

        assert "Résultat: 15" in page.get_result()

    def test_division_by_zero(self, driver):
        page = CalculatorPage(driver)
        page.load_page()
        page.enter_first_number(10)
        page.enter_second_number(0)
        page.select_operation("divide")
        page.click_calculate()

        assert "Erreur: Division par zéro" in page.get_result()

    def test_decimals_number(self, driver):
        page = CalculatorPage(driver)
        page.load_page()
        page.enter_first_number(5.5)
        page.enter_second_number(2.3)
        page.select_operation("add")
        page.click_calculate()

        assert "Résultat: 7.8" in page.get_result()

    def test_neg_number(self, driver):
        page = CalculatorPage(driver)
        page.load_page()
        page.enter_first_number(-2)
        page.enter_second_number(-3)
        page.select_operation("add")
        page.click_calculate()

        assert "Résultat: -5" in page.get_result()

    def test_ui_styles(self, driver):
        page = CalculatorPage(driver)
        page.load_page()

        result_div = page.get_result_element()
        color = result_div.value_of_css_property("background-color")
        padding = result_div.value_of_css_property("padding")

        assert color == "rgba(240, 240, 240, 1)", f"Couleur inattendue: {color}"
        assert padding == "10px"

    def test_all_operations(self, driver):
        page = CalculatorPage(driver)
        page.load_page()

        operations = [
            ("add", "8", "2", "10"),
            ("subtract", "8", "2", "6"),
            ("multiply", "8", "2", "16"),
            ("divide", "8", "2", "4"),
        ]

        for op, num1, num2, expected in operations:
            page.enter_first_number(num1)
            page.enter_second_number(num2)
            page.select_operation(op)
            page.click_calculate()

            assert f"Résultat: {expected}" in page.get_result()
            time.sleep(1)

    def test_page_load_time(self, driver):
        page = CalculatorPage(driver)
        start_time = time.time()
        page.load_page()
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.ID, "calculator")
        )
        load_time = time.time() - start_time
        print(f"Temps de chargement: {load_time:.2f} secondes")

        assert load_time < 3.0, f"Page trop lente à charger: {load_time:.2f}s"

if __name__ == "__main__":
	pytest.main(["-v", "--html=report.html", "--self-contained-html"])