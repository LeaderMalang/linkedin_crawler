from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import random
import requests

class MyFirefoxDriver(Firefox):
    def __init__(self, user_agents=None,is_enable_auto_flags=True,*args, **kwargs):

        # selopt = {}
        # user_proxy=None
        # if proxy is not None and proxy["host"] and proxy["port"]:

        
        self.extension_name=None
        # if extension_url is not None:
        #     self.extension_name=self.download_extension(extension_url)
        #     self.install_addon(self.extension_name, temporary=True)
        self.user_agents = user_agents or ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"]

        options = kwargs.pop('options', None) or FirefoxOptions()
        if is_enable_auto_flags:
            options.set_preference("dom.webdriver.enabled", False)
            options.set_preference('useAutomationExtension', False)
        
        
        super().__init__(*args, options=options, **kwargs)
    def rotate_user_agent(self):
        """Rotates the User-Agent from the pre-defined list by setting a new one."""
        new_user_agent = random.choice(self.user_agents)
        self.profile.set_preference("general.useragent.override", new_user_agent)
        
        # self.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": new_user_agent})
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

    def login_and_save_cookies(self, login_url, login_function, *login_args):
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
        name='extension.xpi'
        with open(name, 'wb') as f:
            f.write(response.content)
        print("Extension downloaded successfully.")
        return name
# Usage of the CustomFirefoxDriver for login and cookie management would be identical to the example provided for CustomChromeDriver.
