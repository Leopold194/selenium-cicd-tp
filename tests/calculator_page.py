import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        file_path = os.path.abspath("../src/index.html")
        self.driver.get(f"file://{file_path}")

    def enter_first_number(self, value):
        el = self.driver.find_element(By.ID, "num1")
        el.clear()
        el.send_keys(str(value))

    def enter_second_number(self, value):
        el = self.driver.find_element(By.ID, "num2")
        el.clear()
        el.send_keys(str(value))

    def select_operation(self, operation):
        select = Select(self.driver.find_element(By.ID, "operation"))
        select.select_by_value(operation)

    def click_calculate(self):
        self.driver.find_element(By.ID, "calculate").click()

    def get_result(self):
        result = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        return result.text

    def get_result_element(self):
        return self.driver.find_element(By.ID, "result")
