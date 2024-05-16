# Requirements
```

This project is about the setup of a system that allows the user to use a selenium webdriver with the browsers Chrome and Firefox.
Further the selenium webdriver should allow the usage of proxies in such a way that the user can enter: host, port, username, and password of the proxy into the selenium driver options. The selenium webdriver-system should not show anyhow that the browser is operated in an automated way.



For this the following steps are proposed:



First identify what kind of automation-identifiers the different browser display in a setup with selenium webdriver. Find an example website on which we can see which identifiers are displayed by the selenium webdriver operated browsers. Then execute measures to stop these identifiers of being displayed.



1. Show widentifiers are displayed when operating without any hiding mechanisms.
2. Use the selenium flags “useAutomationExtension”, “navigator.webdriver” and off course all other that exist to that purpose to hide the automation identifiers. For Chrome and Firefox.
3. Show based on headers how these flags have caused the before found identifiers to disappear.
4. Use use custom headers and header-rotation to adjust the webdrivers header information in order to appear more like a normal user. (Including cockies?)
5. Include the current selenium webdriver for Firefox into selenium in such a way that it inherits from selenium. So that I can import the class from my file and use it like I use a selenium webdriver instance. driver = ChromeDriver(), or FirefoxDriver()
driver.get() instead of now firefoxdriver = mydriver.FirefoxDriver(), firefoxdriver.driver.get()
6. Remove all further flags (‘$cdc_’ , ‘$wdc_’ and all others that occur) that give away that a Chrome or Firefox driver is automated by Selenium.
7. Use Rotating HTTP Header Information and UserAgent to avoid bot detection.
8. Manage Cookies. Periodically update your cookies by relogging in and saving new cookies to maintain an active session.



The goal ist to setup a selenium webdriver systems that allows the usage of linkedin via these webdrivers without the used accounts being flagged as bots.
```


## How to Avoid Bot Detection with Selenium
```
1. Using IP rotation and proxies 
2. Disabling the Automation Indicator WebDriver Flags
3. Rotating HTTP Header Information and UserAgent
4. Avoid Patterns :- To bypass Selenium detection and avoid being identified as a bot, it's important to avoid consistent patterns in your web scraping activities.
5. Remove JavaScript Signature 
6. Using Cookies
7.  Follow The Page Flow
8. Using a Browser Extension

Using a browser extension like uBlock Origin can help block JavaScript challenges and CAPTCHAs, reducing the chances of your bot being detected. 
9. Using a CAPTCHA Solving Service With Selenium

Using a CAPTCHAsolving service like 2Captcha or AntiCaptcha with Selenium can help solve CAPTCHAs that your bot may encounter during web scraping. Here's how you can integrate a CAPTCHAsolving service with Selenium:



```

## Implemention Setups 

### Encapsulate Driver functionalities in MyChromeDriver and MyFirefoxDriver
```

1. Start chrome/firefox service using manager of Chrome and Firefox.
2. Disable automation flags of Chrome and Firefox.
3. Add Proxy
4. Http header information and user agent information.
5. Using Cookies 
  i. Add cookies
  ii. Get cookies
6. Adding any browser extension
```

## Getting Started

### Virtual Environment
```
python -m venv env
```
#### Activate the virtual environment
##### Linux Environment
```
source ./env/bin/activate
```
##### Windows Environment
```
.\env\Script\activate
```
### installing requirements 
 ```
pip install -r requirements.txt
 ```
### Update Environment Variables 
 ```
LINKEDIN_LOGIN_URL=
LINKEDIN_EMAIL=
LINKEDIN_PASSWORD=
PROXY_PORT=
PROXY_HOST=
PROXY_USERNAME=
PROXY_PASSWORD=
CHROME_EXTENSION_URL=
FIREFOX_EXTENSION_URL=

 ```
 #### Start Bot 

 ```
 python main.py
 ```