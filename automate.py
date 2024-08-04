from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a WebDriver instance for Chrome
driver = webdriver.Chrome()

# Replace these placeholders with your actual student ID, password
student_id = "your_id"
password = "your_password"

# Navigate to the student portal login page
driver.get("https://horizon.ucp.edu.pk/web/login")

# Wait for the login input fields and the login button to be visible
wait = WebDriverWait(driver, 10)
student_id_input = wait.until(EC.visibility_of_element_located((By.ID, "login")))
password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-nust.btn-block")))

# Enter the student ID and password
student_id_input.send_keys(student_id)
password_input.send_keys(password)

# Click the login button
login_button.click()

# Wait for the page to load (you may need to adjust the sleep duration based on the page load time)
time.sleep(5)

# Once logged in, you can perform further actions such as navigating to specific pages or extracting data

# Close the browser window
driver.quit()