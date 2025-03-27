import json
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    """Initialize the Appium driver with error handling."""
    try:
        with open("config/config.json", "r") as file:
            capabilities = json.load(file)

        appium_server_url = 'http://localhost:4723'
        driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        
        # Small delay to ensure app launch stability
        time.sleep(3)
        
        return driver

    except FileNotFoundError:
        print("❌ Error: config.json file not found.")
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON format in config.json.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    return None  # Return None if driver initialization fails
