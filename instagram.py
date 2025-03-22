import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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
    time.sleep(2)

def click_helper(element):
    time.sleep(3)
    element.click()
    time.sleep(2)

def wait_element_loading(driver, By, path):
    if By == "XPATH":
        while True:
            try:
                el = driver.find_element(by=AppiumBy.XPATH, value=path)
                return el
            except:
                print(f"No Element Found, {path}")
                time.sleep(2)
    
    if By == "UIA":
        while True:
            try:
                time.sleep(2)
                el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=path)
                return el
            except:
                print(f"No Element Found, {path}")
                time.sleep(2)

def nhan_job_ngay(driver, repeat=0):
    el = wait_element_loading(driver, "XPATH", '//android.widget.TextView[@text="Nhận Job ngay "]')
    click_helper(el)

    try:
        # el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("swal2-content")')
        el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("swal2-content")')
        click_helper(el)
        text = el.text
        if text == 'Vui lòng bấm lại load job !':
            print("Vui lòng bấm lại load job ")

        if text == 'Hiện tại chưa có jobs mới,vui lòng nghỉ tay và quay lại sau 30p nhé !':
            print('Hiện tại chưa có jobs mới,vui lòng nghỉ tay và quay lại sau 30p nhé !')
            if repeat >= 3:
                time.sleep(15)

        el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("OK")')  
        click_helper(el)

        repeat += 1
        nhan_job_ngay(driver, repeat)
    except NoSuchElementException:
        print("Successfull load into job")

def do_job(driver):
    el = wait_element_loading(driver, "XPATH", '//android.view.View[@content-desc="Instagram"]')
    click_helper(el)

    # click on follow button
    try:
        # Code that might raise an exception
        time.sleep(5)
        el = wait_element_loading(driver, "UIA", 'new UiSelector().resourceId("com.instagram.android:id/profile_header_follow_button")') 
        click_helper(el)
    except Exception as e:
        # Code to handle the exception
        print(f"Follow button not available")

def completed_job(driver):
    print("WHAT")
    # Go back to Go Like
    go_to_app(driver)
    # Completed ?
    time.sleep(1)
    el = wait_element_loading(driver, "XPATH", '//android.widget.Button[@text="Hoàn thành"]')
    click_helper(el)

    # Check status message
    el = wait_element_loading(driver,'UIA', 'new UiSelector().resourceId("swal2-title")')
    text = el.text
    if text == "Thành công":
        el = wait_element_loading(driver, "UIA", 'new UiSelector().text("OK")')
        click_helper(el)



# def proccess_flow():
#     nhan_job_ngay(driver, repeat=0)
#     do_job(driver)

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

# Kiem Thuong
# el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Kiếm Thưởng"]')
el = wait_element_loading(driver, "XPATH", '//android.widget.TextView[@text="Kiếm Thưởng"]')
click_helper(el)

# Kiem thuong ngay
# el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("kiếm thưởng ngay ").instance(0)')
el = wait_element_loading(driver, "UIA", 'new UiSelector().text("kiếm thưởng ngay ").instance(0)')
click_helper(el)

# Nhan job ngay
# el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Nhận Job ngay ")')
nhan_job_ngay(driver, repeat=0)
do_job(driver)
completed_job(driver)



