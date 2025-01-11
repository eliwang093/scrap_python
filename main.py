import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# set Chrome options
chrome_options = Options()
# Run Chrome in Incognito Mode
chrome_options.add_argument("--incognito")

# Certain Chrome features by adding arguments:
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# enable detailed logging
chrome_options.add_argument("--log-level=1")

# Initialize undetected-chromedriver
driver = uc.Chrome(options=chrome_options)

try:
    # Navigate to TidyCal website
    driver.get("https://tidycal.com/register")
    print("Website loaded successfully.")

    # Wait for the page to load
    # Need to check this
    time.sleep(5)
    # Wait for the registration form to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

    # Fill in the name field
    name_field = driver.find_element(By.NAME, "name")
    name_field.send_keys("test_user12345")
    print("name tag is found.")

    # Fill in the email field
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("test_user12345@example.com")
    print("email tag is found.")

    # Fill in the password field
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("user123$")
    print("password tag is found.")

    # Optionally, agree to terms if required (add appropriate selector if needed)
    # Example:
    # terms_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    # terms_checkbox.click()

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]")
    submit_button.click()
    print("Form submitted.")

    # Wait for some confirmation or redirection
    time.sleep(5)  # Adjust based on the website's response time

    print("Registration completed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
