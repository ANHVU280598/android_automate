import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException


# appium --port 4723 --log-level info
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

def go_to_app(driver):
    driver.activate_app("com.golike")
    time.sleep(2)

def click_helper(element):
    time.sleep(3)
    element.click()
    time.sleep(2)

def find_by_element(driver, By, path):
    time.sleep(2)
    if By == "XPATH":
            try:
                el = driver.find_element(by=AppiumBy.XPATH, value=path)
                return el
            except:
                print(f"No Element Found, {path}")
                return False
    if By == "UIA":
            try:
                time.sleep(2)
                el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=path)
                return el
            except:
                print(f"No Element Found, {path}")
                return False

def swipe_up(driver, max_swipe, duration=1000):
    try:
        for i in range (max_swipe):
            size = driver.get_window_size()
            start_x = size["width"] / 2
            start_y = size["height"] * 0.8  # Start at 80% of screen height
            end_y = size["height"] * 0.2  # End at 20% of screen height
            driver.swipe(start_x, start_y, start_x, end_y, duration)
        
        return True
    except Exception as e:
        print(f'Error during swipe up')
        return False

def swipe_down(driver, max_swipe, duration=1000):
    try:
        for i in range (max_swipe):
            size = driver.get_window_size()
            start_x = size["width"] / 2
            start_y = size["height"] * 0.2  # Start at 20% of screen height
            end_y = size["height"] * 0.8  # End at 80% of screen height
            driver.swipe(start_x, start_y, start_x, end_y, duration)
        return True
    except Exception as e:
        print(f'Error during swipe down')
        return False

def swipe_to_find(driver, max_swipe, By, path):
    attempts = 0  # Track number of swipes

    while attempts < max_swipe:
        attempts += 1
        if find_by_element(driver, By, path):
            print(f'Found element: {path}')
            return find_by_element(driver, By, path)  # Return found element

        if not swipe_up(driver, max_swipe):
            continue
        
        if not swipe_down(driver, max_swipe):
            continue

    return False  # Return None if element is not found after max_swipe

def handle_click(el, path, retry):
    attempt = 0
    while attempt < retry:
        try:
            el.click()
            return True
        except Exception as e:
            time.sleep(3)
            attempt += 1
            print(f'error when click on: {path}, retry :{attempt}')
            if attempt == 2:
                print("Max attempt reach")
                time.sleep(10000)

def nhan_job_ngay(driver):
    path = 'new UiSelector().text("Nhận Job ngay ")'
    el = swipe_to_find(driver, 1, 'UIA', path)
    # handle_click(el, path, 3)
    if el:
        handle_click(el, path , 1)

    # Check if there are encount an error
    path = '//android.widget.TextView[@resource-id="swal2-content"]'
    el = find_by_element(driver,'XPATH', path)
    if el:
        path = '//android.widget.Button[@text="OK"]'
        handle_click(el, path, 2)
        nhan_job_ngay(driver)
    

def instagram_action(driver):
    # //android.widget.TextView[@text="TĂNG LIKE CHO BÀI VIẾT"]
    # follow-instagram - what if can't find follow button in certain amount of time......
    title = ''
    path_job_title = '//android.widget.TextView[@text="TĂNG LƯỢT THEO DÕI"]'
    path_job_title1 = '//android.widget.TextView[@text="TĂNG LIKE CHO BÀI VIẾT"]'

    title_el = swipe_to_find(driver,1, 'XPATH', path_job_title )
    title_el1 = swipe_to_find(driver,1, 'XPATH', path_job_title1 )

    if title_el:
        title = title_el.text
        print(title)
    if title_el1:
        title = title_el1.text
        print(title)
        return
    
    if title == '':
        print("JOB TITLE DIFFERENT WAIT FOR RECORD")
        print(driver.page_source)
        time.sleep(1000000)


    # launch instagram
    path = 'new UiSelector().description("Instagram")'
    el = swipe_to_find(driver, 2, 'UIA', path)
    handle_click(el, path, 3)



    if title == "TĂNG LƯỢT THEO DÕI":
       path = 'new UiSelector().resourceId("com.instagram.android:id/profile_header_follow_button")' 
       el = swipe_to_find(driver, 2, 'UIA', path)
       if el:
           handle_click(el, path, 2)
           time.sleep(2)
           return True
       else:
           return False
    elif title == "TĂNG LIKE CHO BÀI VIẾT":
        path = 'new UiSelector().resourceId("com.instagram.android:id/row_feed_button_like")'
        if el:
           handle_click(el, path, 2)
           time.sleep(2)
           return True
        else:
           return False
       
    # path1 = 'new UiSelector().resourceId("com.instagram.android:id/row_feed_button_like")'
    
    # el1 = find_by_element(driver, 'UIA', path1)
    # if el:
    #     handle_click(el, path, 3)
    #     return True
    # elif el1:
    #     handle_click(el1, path1, 3)
    #     return True
    # else:
    #     print("Can't find element on instagram: line 132")
    #     return False

def completed_action(driver, is_insta_action_complete):
    if is_insta_action_complete:
    # click on Hoan Thanh
        path = '//android.widget.Button[@text="Hoàn thành"]'
        el = swipe_to_find(driver, 2, 'XPATH', path)
        handle_click(el, path, 3)

        # check status message after finished
        path = 'new UiSelector().resourceId("swal2-title")'
        el = swipe_to_find(driver, 2, 'UIA', path)
        text = el.text
        print(f'Status message = {text}')
        if text == 'Thành công':
            path = '//android.widget.Button[@text="OK"]'
            el = swipe_to_find(driver, 2, 'XPATH', path)
            handle_click(el, path, 3)
        else:
            print("Wait for trouble shoot line 157")
            time.sleep(10000)
    else:
        path = '//android.widget.Button[@text="Báo lỗi"]'
        el = find_by_element(driver, 'XPATH', path)
        handle_click(el, path, 2)

        # Khong tim thay bai viet
        path = '(//android.widget.TextView[@text="radio_button_unchecked"])[4]'
        el = find_by_element(driver, 'XPATH', path)
        handle_click(el, path, 2)

        # Gui bao cao
        path = '//android.widget.Button[@text="Gửi báo cáo"]'
        el = find_by_element(driver, 'XPATH', path)
        handle_click(el, path, 2)
        path = '//android.widget.Button[@text="OK"]'
        el = swipe_to_find(driver, 2, 'XPATH', path)
        handle_click(el, path, 3)





appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
first_run = 0
while True:
    if first_run == 0 :
        # Kiem thuong
        path = '//android.widget.TextView[@text="Kiếm Thưởng"]'
        el = swipe_to_find(driver, 2, 'XPATH', path )
        handle_click(el, path, 3)

        # Kiem thuong ngay
        path = 'new UiSelector().text("kiếm thưởng ngay ").instance(0)'
        el = swipe_to_find(driver, 2, 'UIA', path)
        handle_click(el, path, 3)
        first_run += 1

    # Nhan job ngay - check if need to re-click
    # text = 'Vui lòng bấm lại load job !'
    nhan_job_ngay(driver)

    # instagram_action - should add what job need to do such as follow, comment, ....
    # //android.view.ViewGroup[@resource-id="com.instagram.android:id/coordinator_root_layout"]/android.widget.FrameLayout
    is_insta_action_complete = instagram_action(driver)

    # completed job
    # go back to GOLIKE
    go_to_app(driver)
    completed_action(driver,is_insta_action_complete)






