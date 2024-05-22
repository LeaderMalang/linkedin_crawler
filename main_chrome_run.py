
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from chromeDriver import MyChromeDriver

from logger import set_logger
from linkedin import login_to_linkedin_with_proxy
import os
set_logger()



proxy_host = os.environ['PROXY_HOST'] 
proxy_port = os.environ['PROXY_PORT'] 

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
]

# Install the Chrome Driver
service = ChromeService(ChromeDriverManager().install())

# Download the extension CRX file
extension_url = os.environ['CHROME_EXTENSION_URL'] 
# download_extension(extension_url)

# # Set up Chrome options to load the extension
# chrome_options = Options()

# Initialize the driver with the loaded extension
driver = MyChromeDriver(service=service, user_agents=user_agents,extension_url=extension_url)

print('Successfully added extension!')

# Rotate user agents
driver.rotate_user_agent()  

# Login URL
login_url = os.environ['LINKEDIN_LOGIN_URL'] 

# Perform login and save cookies
cookies = driver.login_and_save_cookies(login_url, login_to_linkedin_with_proxy)

# Add cookies to the driver
driver.add_cookies(cookies)

# Additional actions using the driver, if any
specific_cookie = driver.get_cookie('session_cookie_name')
all_cookies = driver.get_all_cookies()
