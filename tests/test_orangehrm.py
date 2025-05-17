from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.employee_list_page import EmployeeListPage
from utils.driver_setup import get_driver

driver = get_driver()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Login
login = LoginPage(driver)
login.enter_username("Admin")
login.enter_password("admin123")
login.click_login()

# Navigate to PIM
dashboard = DashboardPage(driver)
dashboard.go_to_pim()

# Add Employees
pim = PIMPage(driver)
names = [("Alice", "Smith"), ("Bob", "Brown"), ("Carol", "Jones"), ("David", "Lee")]
for first, last in names:
    pim.click_add_employee()
    pim.add_employee(first, last)

# Verify Employees
emp_list = EmployeeListPage(driver)
for first, last in names:
    full_name = f"{first} {last}"
    emp_list.search_employee(full_name)
    emp_list.verify_employee(full_name)

# Logout
dashboard.logout()
driver.quit()