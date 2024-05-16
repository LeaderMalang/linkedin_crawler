from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time
import os
from fireFoxDriver import MyFirefoxDriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import logging
from webdriver_manager.core.logger import set_logger

logger = logging.getLogger("custom_logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.FileHandler("custom.log"))

set_logger(logger)



def login_to_linkedin_with_proxy(driver):
    try:
        email = 'razis928@gmail.com'  # Set email here
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_key")))
        email_field.send_keys(email)
        
        password = 'shah1122'  # Set password here
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

proxy_host = "203.124.53.122"
proxy_port = 5678

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
]

# Install the Chrome Driver
service = FirefoxService(GeckoDriverManager().install())

# Download the extension CRX file
extension_url = "https://addons.mozilla.org/en-US/firefox/addon/get-rss-feed-url/latest.xpi"


# Set up Firefox profile
profile = FirefoxProfile()

# Initialize the driver with the loaded extension
driver = MyFirefoxDriver(service=service, user_agents=user_agents,proxy={
   "host": proxy_host,
   "port":proxy_port
},profile=profile)
path_addon=os.path.abspath(os.path.join(os.getcwd(), "extension.xpi"))
# extension_name=driver.download_extension(extension_url)
driver.install_addon("C:\\Users\\ACS\\AppData\\Local\\Temp\\extension.xpi", temporary=True)
print('Successfully added extension!')
# Rotate user agents
driver.rotate_user_agent()  

# Login URL
login_url = 'https://www.linkedin.com/'

# Perform login and save cookies
cookies = driver.login_and_save_cookies(login_url, login_to_linkedin_with_proxy)

# Add cookies to the driver
driver.add_cookies(cookies)

# Additional actions using the driver, if any
specific_cookie = driver.get_cookie('session_cookie_name')
all_cookies = driver.get_all_cookies()
