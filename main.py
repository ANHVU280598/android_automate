import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.golike',
    appActivity='com.golike.MainActivity',
    language='en',
    noReset= True,
    fullReset= False,
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def click_earn_reward(self)-> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='new UiSelector().text("Kiếm Thưởng")')
        el.click()
        time.sleep(1)

    def instagram_earn(self)->None:
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("kiếm thưởng ngay ").instance(0)')
        el.click()
        time.sleep(1)

    def job(self)->None:
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Nhận Job ngay ")')
        time.sleep(1)
        
    
    def click_instagram_earn(self)->None:
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Instagram")')
        el.click()
        time.sleep(1)

    def follow_instagram(self)->None:
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("com.instagram.android:id/profile_header_follow_button")')
        el.click()
        time.sleep(1)
           
    def go_to_app(self)->None:
        self.driver.activate_app("com.golike")
        time.sleep(1)

    def complete(self)->None:
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Hoàn thành")')
        el.click()
        time.sleep(1)
        # Check status message
        el = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("swal2-title")')
        text = el.text
        if text == "Thành công":
            el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("OK")')
            el.click()
        time.sleep(1)




    



# new UiSelector().text("Báo lỗi")
# new UiSelector().text("Không tìm thấy bài viết")
        


if __name__ == '__main__':
    unittest.main()