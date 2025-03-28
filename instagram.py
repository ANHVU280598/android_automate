from automation_base.Base import Base
import time

class Instagram:
    def __init__(self):
        self.base = Base()
        self.driver = self.base.driver

    def by_pass_anouncement(self):
        path = '//android.widget.Button[@text="Đã hiểu"]'
        return self.base.click_on_element('XPATH', path)
    
    def click_kiem_thuong(self):
        path = '//android.widget.TextView[@text="Kiếm Thưởng"]'
        return self.base.click_on_element('XPATH', path)

    def click_instagram(self):
        path = '(//android.widget.TextView[@text="kiếm thưởng ngay "])[1]'
        return self.base.click_on_element('XPATH', path)

    def click_nhan_job_ngay(self, retry = 3, delay = 3):
        self.driver.activate_app('com.golike')
        if retry == 0:
            return False

        path = 'new UiSelector().text("Nhận Job ngay ")'
        self.base.click_on_element('UIA', path)
        
        path = '//android.view.View[@resource-id="app"]/android.view.View/android.view.View[2]/android.view.View[1]//android.widget.TextView'
        job_title = self.base.get_element_text('XPATH', path)
        if job_title:
            print("legit")
            return job_title

        # Check if any other anouncement pop up
        path = '//android.widget.TextView[@resource-id="swal2-content"]'
        if self.base.advance_is_element_present('XPATH', path):
            path = '//android.widget.Button[@text="OK"]'
            self.base.click_on_element('XPATH', path)
            return self.click_nhan_job_ngay(retry - 1)
        
    
    def increase_follwer_job(self):
        path = 'new UiSelector().resourceId("com.instagram.android:id/profile_header_follow_button")'
        if self.base.click_on_element("UIA", path):
            return True
        return False

    def increase_like_job(self):
        path = 'new UiSelector().resourceId("com.instagram.android:id/row_feed_button_like")'
        if self.base.click_on_element("UIA", path):
            return True
        return False
    
    def send_report(self):
        self.base.go_to_app()
        path = '//android.widget.Button[@text="Báo lỗi"]'
        self.base.click_on_element("XPATH", path)

        # Khong tim thay bai viet
        path = '(//android.widget.TextView[@text="radio_button_unchecked"])[4]'
        self.base.click_on_element("XPATH", path)

        # Gui bao cao 
        path = '//android.widget.Button[@text="Gửi báo cáo"]'
        self.base.click_on_element("XPATH", path)

        # Click Ok Btn
        path = '//android.widget.Button[@text="OK"]'
        self.base.click_on_element("XPATH", path)

        return True

    def do_job_title(self):
        job_title = self.click_nhan_job_ngay()

        path = '//android.view.View[@content-desc="Instagram"]'
        self.base.click_on_element("XPATH", path)

        result = None
        if job_title == "TĂNG LƯỢT THEO DÕI":
            result = self.increase_follwer_job()
        elif job_title == "TĂNG LIKE CHO BÀI VIẾT":
            result = self.increase_like_job()
        else:
            result = "new case"
            time.sleep(10000)

        if result == False:
            return self.send_report()
        
        return True

    def complete_job(self, delay=3):
        self.base.go_to_app()
        time.sleep(delay)
        path = '//android.widget.Button[@text="Hoàn thành"]'
        self.base.click_on_element('XPATH', path)
        path = '//android.widget.Button[@text="OK"]'
        self.base.click_on_element('XPATH', path)
        return True

if __name__ == "__main__":
    bot = Instagram()

    while True:
        if bot.click_kiem_thuong() == False:
            break

        if bot.click_instagram() == False:
            break
        if bot.do_job_title() == False:
            break
        if bot.complete_job() == False:
            break



    
