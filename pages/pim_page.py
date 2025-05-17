from selenium.webdriver.common.by import By

class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_employee(self):
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()

    def add_employee(self, first_name, last_name):
        self.driver.find_element(By.NAME, "firstName").send_keys(first_name)
        self.driver.find_element(By.NAME, "lastName").send_keys(last_name)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()