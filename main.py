
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from chromeDriver import MyChromeDriver
def login_to_linkedin_with_proxy(driver,email, password):
    
    
    
    try:
        
        
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_key")))
    
        email_field.send_keys(email)
        
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_password")))
        password_field.send_keys(password)

        
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("https://www.linkedin.com/feed/")
        )
        
        print("Login successful!")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
        
    except Exception as e:
        print("Error during login:", e)
        
    finally:
        driver.quit()

email = "razis928@gmail.com"
password = "shah1122"
proxy_host = "203.124.53.122"
proxy_port = 5678

# login_to_linkedin_with_proxy(email, password, proxy_host, proxy_port)



service = ChromeService(ChromeDriverManager().install())
# Instantiate your custom Chrome driver.
driver = CustomChromeDriver(service=service)

# Define credentials and login URL.
login_url = 'https://www.linkedin.com/'
credentials = {'email': email, 'password': shah1122}

# Perform login and get cookies afterward.
cookies = driver.login_and_save_cookies(login_url, login_to_linkedin_with_proxy, **credentials)

# Add cookies to the driver.
driver.add_cookies(cookies)

# Get an individual cookie by name.
specific_cookie = driver.get_cookie('session_cookie_name')

# Get all cookies.
all_cookies = driver.get_all_cookies()