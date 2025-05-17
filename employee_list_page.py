from selenium.webdriver.common.by import By

class EmployeeListPage:
    def __init__(self, driver):
        self.driver = driver

    def search_employee(self, name):
        search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
        search_input.send_keys(name)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def verify_employee(self, name):
        results = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']//div[2]")
        for result in results:
            if name in result.text:
                print("Name Verified:", name)
                return True
        return False