from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_pim(self):
        pim_menu = self.driver.find_element(By.LINK_TEXT, "PIM")
        ActionChains(self.driver).move_to_element(pim_menu).click().perform()

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()