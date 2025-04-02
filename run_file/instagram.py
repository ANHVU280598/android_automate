from automation_base.Base import Base
import time

class Instagram:
    def __init__(self):
        self.base = Base()
        self.driver = self.base.driver

    def by_pass_anouncement(self):
        self.base.current_package()
        self.base.terminate_app()
        path = '//android.widget.Button[@text="Đã hiểu"]'
        return self.base.click_on_element('XPATH', path)
    
    def click_kiem_thuong(self):
        path = '//android.widget.TextView[@text="Kiếm Thưởng"]'
        return self.base.click_on_element('XPATH', path)

    def click_instagram(self):
        path = '//android.widget.TextView[@text="Instagram"]'
        return self.base.click_on_element('XPATH', path)

    def click_nhan_job_ngay(self, retry = 3, delay = 3):
        if retry == 0:
            return False

        path = 'new UiSelector().text("Nhận Job ngay ")'
        self.base.click_on_element('UIA', path)
        
        path = '//android.view.View[@resource-id="app"]/android.view.View/android.view.View[2]/android.view.View[1]//android.widget.TextView'
        job_title = self.base.get_element_text('XPATH', path)
        if job_title == "TĂNG LƯỢT THEO DÕI" or job_title == "TĂNG LIKE CHO BÀI VIẾT":
            print(job_title)
            return job_title

        # Check if any other anouncement pop up
        path = '//android.widget.TextView[@resource-id="swal2-title"]'
        anounment_text = bot.base.get_element_text('XPATH', path)

        if anounment_text == 'Thông báo':
            time.sleep(20)
            print("TAKE BREAK")
            path = '//android.widget.Button[@text="OK"]'
            self.base.click_on_element('XPATH', path)
            return self.click_nhan_job_ngay(retry = 3)
            
        if anounment_text == 'Thành công':
            path = '//android.widget.Button[@text="OK"]'
            self.base.click_on_element('XPATH', path)
        else:
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
    def post_comment_job(self):
        path = '//android.widget.TextView[@text="Click để Copy bình luận"]'
        self.base.click_on_element("XPATH", path)

    def send_report(self):
        self.base.go_to_app()
        self.base.terminate_app()
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
        path = '//android.view.View[@resource-id="app"]/android.view.View/android.view.View[2]/android.view.View[1]//android.widget.TextView'
        job_title = self.base.get_element_text('XPATH', path)
        print(job_title)


        path = '//android.view.View[@content-desc="Instagram"]'
        self.base.click_on_element("XPATH", path)
        time.sleep(5)

        result = False
        if job_title == "TĂNG LƯỢT THEO DÕI":
            result = self.increase_follwer_job()
        elif job_title == "TĂNG LIKE CHO BÀI VIẾT":
            result = self.increase_like_job()
        elif job_title == "TĂNG LƯỢT COMMENT":
            return
        else:
            result = "new case"

        if result == False:
            print("Result is False")
            return self.send_report()
        else:
            return self.complete_job()


    def complete_job(self, delay=3):
        self.base.go_to_app()
        self.base.terminate_app()
        time.sleep(delay)
        path = '//android.widget.Button[@text="Hoàn thành"]'
        self.base.click_on_element('XPATH', path)
        path = '//android.widget.Button[@text="OK"]'
        self.base.click_on_element('XPATH', path)
        return True

if __name__ == "__main__":
    bot = Instagram()
    bot.base.current_package()




    # # bot.by_pass_anouncement()
    # reset_app = False
    # while True:
    #     bot.base.go_to_app()

    #     if reset_app:
    #         bot.base.terminate_app('com.golike')
    #         bot.base.quit_driver()
    #         bot = Instagram()
    #         time.sleep(5)
    #         reset_app = False

    #     if not bot.click_kiem_thuong():
    #         reset_app = True
    #         continue
    #     else:
    #         reset_app = False
        
    #     if not bot.click_instagram():
    #         reset_app = True
    #         continue
    #     else:
    #         reset_app = False

    #     if not bot.click_nhan_job_ngay():
    #         reset_app = True
    #         continue
    #     else:
    #         reset_app = False

    #     bot.do_job_title()

        # bot.complete_job()



    
