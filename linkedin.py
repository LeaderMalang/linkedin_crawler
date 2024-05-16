from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
def login_to_linkedin_with_proxy(driver):
    try:
       # Set email here
        email = os.environ['LINKEDIN_EMAIL'] 
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_key")))
        email_field.send_keys(email)
        
        password = os.environ['LINKEDIN_PASSWORD']   # Set password here
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_password")))
        password_field.send_keys(password)

        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        WebDriverWait(driver, 10).until(EC.url_contains("https://www.linkedin.com/feed/"))
        
        print("Login successful!")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            
            # Check if the button exists
            try:
                button = driver.find_element(By.CSS_SELECTOR, "button.artdeco-button.artdeco-button--secondary.mv5.t-14.t-black.t-normal")
                button.click()
                print("Clicked 'See new posts' button.")
            except NoSuchElementException:
                pass
        
    except Exception as e:
        print("Error during login:", e)
        
    finally:
        driver.quit()

