from drivers.Driver import get_driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self):
        self.driver = get_driver()
        self.wait  = WebDriverWait(self.driver, 5)
        
    def go_to_app(self, delay=3):
        self.driver.activate_app("com.golike")
        time.sleep(delay)
        return True

    def current_package(self, app_name='com.golike'):
        self.driver.app_strings
        current_package = self.driver.current_package
        current_activity = self.driver.current_activity
        print(f'Current active app {current_package}')
        print(f'Current active app {current_activity}')
        if current_package != app_name:
            self.driver.activate_app(app_name)

    def terminate_app(self, app_name='com.instagram.android'):
        os.system(f'adb shell am force-stop {app_name}')
        print(f"{app_name} has been force-stoppped.")

    def btn_back(self):
        self.driver.press_button(4)
        return True
    
    def get_text_value_from_clipboard(self):
        return self.driver.get_clipboard_text()

    def quit_driver(self):
        self.driver.quit()
    # def swipe_up(self, max_swipe, duration=1000):
    #     try:
    #         for i in range (max_swipe):
    #             size = self.driver.get_window_size()
    #             start_x = size["width"] / 3
    #             start_y = size["height"] * 0.9  # Start at 80% of screen height
    #             end_y = size["height"] * 0.2  # End at 20% of screen height
    #             self.driver.swipe(start_x, start_y, start_x, end_y, duration)         
    #         return True
    #     except Exception as e:
    #         print(f'Error during swipe up')
    #         return None

    # def swipe_down(self, max_swipe, duration=1000):
    #     try:
    #         for i in range (max_swipe):
    #             size = self.driver.get_window_size()
    #             start_x = size["width"] / 3
    #             start_y = size["height"] * 0.2  # Start at 20% of screen height
    #             end_y = size["height"] * 0.9  # End at 80% of screen height
    #             self.driver.swipe(start_x, start_y, start_x, end_y, duration)
    #         return True
    #     except Exception as e:
    #         print(f'Error during swipe down {e}')
    #         return False

    # def swipe(self, max_swipe = 2):
    #     self.swipe_up(max_swipe, duration=1000)
    #     self.swipe_down(max_swipe, duration=1000)
    #     return True

    def scroll_to_view(self, text):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(text("{text}"))')
    
    def is_element_present(self, By, path):
        try:
            if By == "XPATH":
                el = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, path)))
            elif By == "UIA":
                el = self.wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, path)))
            return el
        except Exception:
            return False
        

    def _perform_action_with_retry(self, By, path, action, retry=2, delay = 2):
        """
        Perform an action (like click or get text) with retry logic.
        :param By: The method to locate the element (e.g., By.XPATH)
        :param path: The XPath or selector for the element
        :param action: The action to perform (e.g., el.click, el.text)
        :param retry: The number of retry attempts
        :return: The result of the action (True for success, False for failure)
        """
        attempt = 0
        while attempt < retry:
            el = self.is_element_present(By, path)
            if el:
                try:
                    result = action(el)
                    print(f"Successfully performed action on element: {path}")
                    return True
                except Exception as e:
                    print(f"Error performing action on element: {path}")
                    return False
            else:
                print(f"Element not found/clickable/textable, attempt {attempt + 1}/{retry}")                
                attempt += 1
        print(f"Failed to perform action on element: {path} after {retry} attempts")
        return False
    
    def click_on_element(self, By, path):
        return self._perform_action_with_retry(By, path, lambda el: el.click())
    
    def send_keys(self, By, path):
        return self._perform_action_with_retry(By, path, lambda el : el.send_keys(self.get_text_value_from_clipboard))

    def get_element_text(self, By, path, delay = 3, retry = 2):
        attempt = 0
        time.sleep(delay)
        while attempt < retry:
            el = self.is_element_present(By, path)
            if el:
                try:
                    time.sleep(delay)
                    # Perform the desired action
                    result = el.text
                    print(f"Successfully performed action on element: {path}")
                    return result
                except Exception as e:
                    print(f"Error performing action on element: {path}")
                    return False
            else:
                print(f"Element not found/clickable/textable, attempt {attempt + 1}/{retry}")                
                attempt += 1
        print(f"Failed to perform action on element: {path} after {retry} attempts")
        return False
    