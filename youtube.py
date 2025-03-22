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
    noReset=True,
    fullReset=False,
    locale='US'
)

def go_to_app(driver):
    driver.activate_app("com.golike")
    time.sleep(1)

def click_helper(element):
    element.click()
    time.sleep(1)

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

# Kiem Thuong - Youtube
el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Kiếm Thưởng"]')
click_helper(el)

# Kiem thuong ngay
el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("kiếm thưởng ngay ").instance(4)')
click_helper(el)

# Nhan job ngay
el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Nhận Job ngay ")')
click_helper(el)
try:
    el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("swal2-content")')
    click_helper(el)
    text = el.text

    if text == 'Vui lòng bấm lại load job !':
        print("Vui lòng bấm lại load job ")

    if text == 'Hiện tại chưa có jobs mới,vui lòng nghỉ tay và quay lại sau 30p nhé !':
        print('Hiện tại chưa có jobs mới,vui lòng nghỉ tay và quay lại sau 30p nhé !')
        time.sleep(1800)

    el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("OK")')
    click_helper(el)

    el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Nhận Job ngay ")')
    click_helper(el)
except:
    print("Successfull load into job")


# redirect to Youtube (maybe check condition if the mission is different than just follow)
el = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[contains(@content-desc, "Subscribe")]')
click_helper(el)



# # click on follow button
# try:
#     # Code that might raise an exception
#     el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("com.instagram.android:id/profile_header_follow_button")')
#     click_helper(el)
# except Exception as e:
#     # Code to handle the exception
#     print(f"Follow button not available")



# # Go back to Go Like
# go_to_app(driver)

# # Completed ?
# el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Hoàn thành")')
# click_helper(el)

# # Check status message
# el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("swal2-title")')
# text = el.text
# if text == "Thành công":
#     el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("OK")')
#     click_helper(el)
