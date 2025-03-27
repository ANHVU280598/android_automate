from drivers.Driver import get_driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Base:
    def __init__(self):
        self.driver = get_driver()
        
    def go_to_app(self, delay=3):
        self.driver.activate_app("com.golike")
        time.sleep(2)

    def swipe_up(self, max_swipe, duration=1000):
        try:
            for i in range (max_swipe):
                size = self.driver.get_window_size()
                start_x = size["width"] / 2
                start_y = size["height"] * 0.8  # Start at 80% of screen height
                end_y = size["height"] * 0.2  # End at 20% of screen height
                self.driver.swipe(start_x, start_y, start_x, end_y, duration)         
            return True
        except Exception as e:
            print(f'Error during swipe up')
            return None

    def swipe_down(self, max_swipe, duration=1000):
        try:
            for i in range (max_swipe):
                size = self.driver.get_window_size()
                start_x = size["width"] / 2
                start_y = size["height"] * 0.2  # Start at 20% of screen height
                end_y = size["height"] * 0.8  # End at 80% of screen height
                self.driver.swipe(start_x, start_y, start_x, end_y, duration)
            return True
        except Exception as e:
            print(f'Error during swipe down')
            return None

    def swipe(self, max_swipe = 2):
        self.swipe_up(max_swipe, duration=1000)
        self.swipe_down(max_swipe, duration=1000)

    def is_element_present(self, By, path):
        try:
            if By == "XPATH":
                el = self.driver.find_element(by=AppiumBy.XPATH, value=path)
            elif By == "UIA":
                el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=path)
            else:
                return None
            return el
        except Exception:
            return None
        
    def advance_is_element_present(self, By, path, retry = 2, delay = 5):
        result = self.is_element_present(By, path)

        if retry == 0:
            print(f'Cannot found element: {path}')
            return None
        
        if result is not None:
            return result
        
        self.swipe()

        print(f" Element not found: {path}.")
        time.sleep(delay)
        return self.advance_is_element_present(By, path, retry - 1)

    def _perform_action_with_retry(self, By, path, action, retry=2, delay = 5):
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
            el = self.advance_is_element_present(By, path)
            if el:
                try:
                    time.sleep(delay)
                    # Perform the desired action
                    result = action(el)
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
    
    def click_on_element(self, By, path):
        return self._perform_action_with_retry(By, path, lambda el: el.click())

    def get_element_text(self, By, path):
        text = self._perform_action_with_retry(By, path, lambda el: el.text)
        print(text)
        return text