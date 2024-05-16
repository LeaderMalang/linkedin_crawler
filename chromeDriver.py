from selenium.webdriver import  Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import requests
import os
class MyChromeDriver(Chrome):

  def __init__(self,user_agents=None, extension_url=None, *args, **kwargs):
    
    proxy = kwargs.get('proxy', None) 
    # extension_url = kwargs.get('extension_url', None) 
    self.extension_name=None
    if extension_url is not None:
       self.extension_name=self.download_extension(extension_url)
    self.user_agents = user_agents or ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"]

    options = kwargs.get('options', None) or ChromeOptions()
    #set Proxy options
    if proxy is not None:
       
      options.add_argument('--proxy-server=%s:%s' % (proxy[0], proxy[1]))
    #user agents
    options.add_argument(f"user-agent={random.choice(self.user_agents)}")
    # Set custom options to disable automation flags
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")
    if self.extension_name is not None:
       
      options.add_argument(f"--load-extension={os.path.abspath(os.path.join(os.getcwd(), self.extension_name))}")

    super().__init__(*args, **kwargs)

  def rotate_user_agent(self):
        """Rotates the User-Agent from the pre-defined list by setting a new one."""
        new_user_agent = random.choice(self.user_agents)
        self.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": new_user_agent})
        print(f"User-Agent rotated to: {new_user_agent}")

  def add_cookie(self, cookie_dict):
    """
        Adds a single cookie to your current session.
        :param cookie_dict: A dictionary object with details for the cookie: 
                            {'name': 'cookie_name', 'value': 'cookie_value', ...}
    """
    super().add_cookie(cookie_dict)

  def add_cookies(self, cookies):
    """
        Adds a list of cookies to your current session.
        :param cookies: A list of dictionaries where each dict contains 
                        details for a single cookie to be added.
    """
    for cookie in cookies:
      self.add_cookie(cookie)

  def get_cookie(self, name):

    """
        Get a single cookie by name. Returns the cookie if found, None if not.
        :param name: Name of the cookie.
    """
    return super().get_cookie(name)

  def get_all_cookies(self):
    """
        Returns a list of all cookies in the current session.
    """
    return super().get_cookies()

  def login_and_save_cookies(self, login_url, login_function, **login_args):
    """
        Perform login and then save the cookies post-login.
        :param login_url: The URL to navigate to for login.
        :param login_function: A function to call to perform login actions.
                               This function should accept a driver instance as its first argument,
                               followed by any *login_args. 
        :param login_args: Arguments necessary to perform the login provided to login_function.
    """
    # Navigate to the login page
    self.get(login_url)
    # Execute the login action, passing this driver instance and any other login args
    login_function(self, *login_args)
        # Save cookies after login
    return self.get_all_cookies()
  
  def download_extension(self,extension_url):
    response = requests.get(extension_url)
    name='extension.crx'
    with open(name, 'wb') as f:
        f.write(response.content)
    print("Extension downloaded successfully.")
    return name
    

    
