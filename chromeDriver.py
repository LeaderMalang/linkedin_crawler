from selenium.webdriver import  Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
class MyChromeDriver(Chrome):

  def __init__(self, *args, **kwargs):
    
    proxy = kwargs.pop('proxy', None) 
    
    options = kwargs.pop('options', None) or ChromeOptions()
    #set Proxy options
    chrome_options.add_argument('--proxy-server=%s:%s' % (proxy[0], proxy[1]))
    # Set custom options to disable automation flags
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")
    super().__init__(*args, **kwargs)
    

    
