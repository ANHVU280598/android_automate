from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    try:
        # Appium capabilities
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='R5CW823HW4K',
            appPackage='com.golike',
            appActivity='com.golike.MainActivity',
            language='en',
            noReset=True,
            fullReset=False,
            locale='US'
        )
        
        appium_server_url = 'http://localhost:4723/wd/hub'

        # Attempt to start the driver
        driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

        print("Driver initialized successfully.")
        return driver
    
    except Exception as e:
        print(f"Error initializing Appium driver check get_driver.py")
        return None  # Return None if initialization fails

