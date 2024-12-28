# Selenium WebDriver Automation - Login Test

This project is an automation script using **Selenium WebDriver** to perform login tests on the Jubelio platform.

## Prerequisites

Before running the automation script, you need to have the following installed:

1. **Python** (Version 3.x) - You can download it from [python.org](https://www.python.org/downloads/).
2. **Selenium** - Python package for Selenium WebDriver.
   - Install Selenium by running the following command:
     ```bash
     pip install selenium
     ```
3. **Chrome WebDriver** (or your preferred browser's WebDriver) - Required for controlling the Chrome browser through Selenium.
   - Download the appropriate version of **[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)** based on your Chrome version and place it in the project folder.
   
4. **Text Editor/IDE** - Any text editor like Visual Studio Code, PyCharm, or Sublime Text for editing the code.

## Project Setup

1. **Clone or Download the Repository**:
   - If you are using version control, clone the repository using:
     ```bash
     git clone <repository_url>
     ```
   - Or download the project folder as a ZIP file and extract it.

2. **Place the ChromeDriver in the Project Folder**:
   - Download **ChromeDriver** from the link above and place the executable (`chromedriver.exe`) in the root of your project folder.

3. **Edit the Automation Script**:
   - Open the `login_test.py` script in your text editor.
   - Make sure to replace the placeholders for `email` and `password` with your actual test credentials:
     ```python
     driver.find_element(By.NAME, "email").send_keys("your_email@gmail.com")
     driver.find_element(By.NAME, "password").send_keys("your_password")
     ```

4. **Configure the Path to ChromeDriver**:
   - Update the `executable_path` in the script to the location of your **ChromeDriver**.
   ```python
   driver = webdriver.Chrome(executable_path='./chromedriver.exe')
