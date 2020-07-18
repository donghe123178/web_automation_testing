from config import config
from selenium.webdriver.common.by import By
from common.base_page import BasePage
import time


class StudentsPage(BasePage):
    """Students页面操作：私信操作
        1.定位全部学生，点击
        2.定位第一个学生，鼠标悬停
        3.定位call图标，点击
        4.定位会话输入框
        5.输入消息
        6.定位发送按钮
        7.点击提交，等待发送成功
        8.定位发送的文本，最新的
    """
    url = config.HOST + "/StudentsV2/index/courseid/MDAwMDAwMDAwMLR2vd6Gz8mw.html"

    all_students_locator = (By.XPATH, '//li[contains(@class, "all")]')
    fist_student_locator = (By.XPATH, '//p[@class="studentavatar"]/..')
    call_locator = (By.XPATH, '//a[@class="call"]')
    input_message_locator = (By.XPATH, '//textarea[@class="ps-container"]')
    send_btn_locator = (By.XPATH, '//a[contains(@class,"btn-positive")]')
    message_locator =(By.XPATH, '(//div[@class="text"])[last()]')

    def get(self):
        """刷新页面"""
        self.driver.get(self.url)
        return self

    def send_message(self, message):
        """私信操作"""
        students = self.find(self.all_students_locator)
        students.click()
        self.move_to(self.fist_student_locator)
        call_btn = self.wait_element_visible(self.call_locator)
        call_btn.click()
        input_message = self.find(self.input_message_locator)
        input_message.send_keys(message)
        self.click_element(self.send_btn_locator)
        # time.sleep(10)
        e = self.find(self.message_locator)
        return e.text


