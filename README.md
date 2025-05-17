
# OrangeHRM Automation Assignment (QA Intern 2025)

This project is a part of the QA Intern Assignment 2025, where we analyze, manually test, and automate workflows of the [OrangeHRM](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) web application. It demonstrates the use of Selenium with Python, following the Page Object Model (POM) design pattern.

---

## 📌 Objectives

- ✅ Analyze the application and identify key test scenarios
- 🧪 Write manual test cases for login and employee management
- 🐞 Identify potential bugs and usability issues
- 🤖 Automate key workflows using Selenium with POM

---

## 🔧 Tech Stack

- **Language:** Python
- **Framework:** Selenium WebDriver
- **Design Pattern:** Page Object Model (POM)
- **Browser:** Chrome (via ChromeDriver)

---

## 📂 Project Structure

```
orangehrm_automation/
│
├── pages/               # Page Object classes (Login, Dashboard, PIM, Employee List)
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── pim_page.py
│   └── employee_list_page.py
│
├── tests/               # Test scripts
│   └── test_orangehrm.py
│
├── utils/               # Utility functions (driver setup)
│   └── driver_setup.py
│
└── README.md            # This file
```

---

## ✅ Automated Workflow Covered

1. **Login to the application**
2. **Navigate to the PIM module**
3. **Add 3–4 employees**
4. **Verify employees in the Employee List**
5. **Print "Name Verified" upon match**
6. **Log out of the application**

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install selenium
   ```

2. Download and place [ChromeDriver](https://sites.google.com/chromium.org/driver/) in your PATH.

3. Run the test:
   ```bash
   python tests/test_orangehrm.py
   ```

---

## 🧪 Manual Test Cases

Manual test cases for login and employee management are provided in the [TestCases_Document.pdf](link-if-uploaded).

---

## 🐞 Identified Issues (Examples)

1. No error shown for empty fields unless submit is clicked
2. No rate-limiting for invalid login attempts
3. Password field does not mask special characters properly

---

## 🎥 Loom Walkthrough

A short Loom video explaining this project can be found [here](link-to-loom-video).

---

## 📬 Contact

For any questions or clarifications, feel free to reach out at:  
**Your Name** - [your.email@example.com]
