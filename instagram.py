from automation_base.Base import Base


if __name__ == '__main__':
    base = Base()
    while True:
        # CLick Kiem Thuong
        path = '//android.widget.TextView[@text="Kiếm Thưởng"]'
        base.click_on_element('XPATH', path)

        # Click Instagram
        path = '//android.widget.TextView[@text="Instagram"]'
        base.click_on_element('XPATH', path)

        # Click Nhan Job Ngay
        path = '//android.widget.TextView[@text="Nhận Job ngay "]'
        base.click_on_element('XPATH', path)

    



    
