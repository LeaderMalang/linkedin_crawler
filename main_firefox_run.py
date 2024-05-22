
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
import os
from fireFoxDriver import MyFirefoxDriver
from logger import set_logger
from linkedin import login_to_linkedin_with_proxy
set_logger()




proxy_host = os.environ['PROXY_HOST'] 
proxy_port = os.environ['PROXY_PORT'] 

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
]

# Install the Chrome Driver
service = FirefoxService(GeckoDriverManager().install())

# Download the extension CRX file
extension_url = os.environ['FIREFOX_EXTENSION_URL']




# Initialize the driver with the loaded extension
driver = MyFirefoxDriver(service=service, user_agents=user_agents,proxy={
   "host": proxy_host,
   "port":proxy_port
})
path_addon=os.path.abspath(os.path.join(os.getcwd(), "extension.xpi"))
# extension_name=driver.download_extension(extension_url)
driver.install_addon("C:\\Users\\ACS\\AppData\\Local\\Temp\\extension.xpi", temporary=True)
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
