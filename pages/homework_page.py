from config import config
from selenium.webdriver.common.by import By
from common.base_page import BasePage
import logging
import time


class HomeWorkPage(BasePage):
    """作业页面操作：
        1. 添加作业文件
        2. 提交
        3. 作业留言:
            6.定位作业留言按钮，点击<br/>
            7.定位留言输入框<br/>8.输入留言<br/>
            9.定位保存按钮，点击提交<br/>
            10.定位作业留言按钮，获取留言信息，断言
        4. 查看提交日志

    """
    url = config.HOST + "/Homework/handup/homeworkid/MDAwMDAwMDAwMLScz5mHqa9s.html"

    # 更新提交
    submit_btn_locator = (By.XPATH, '//a[contains(@class, "tj-btn")]')
    new_submit_btn1_locator = (By.XPATH, '//a[@class="new-tj1"]')
    new_submit_btn2_locator = (By.XPATH, '//a[contains(@class, "new-tj2")]')

    sure_btn_locator = (By.XPATH, '//div[@class="btns"]//a[contains(@class, "active")]')

    add_files_btn_locator = (By.XPATH, '//input[@name="file"]')

    delete_file_btn_locator = (By.XPATH, '//a[text()="删除"]')

    success_message_locator = (By.XPATH, '//div[@class="weui_dialog_bd"]')
    known_locator = (By.XPATH, '//a[contains(@class, "weui_btn_dialog")]')

    message_btn_locator = (By.XPATH, '//span[@class="s2"]')
    comment_locator = (By.XPATH, '//textarea[@id="comment"]')
    save_btn_locator = (By.XPATH, '//textarea[@id="comment"]/following-sibling::a')

    view_status_locator = (By.XPATH, '//a[@class="togglesee"]')
    log_locator = (By.XPATH, '//div[@class="content"]//li//p')

    def get(self):
        """刷新页面"""
        self.driver.get(self.url)
        return self

    def upload_files(self, file_path):
        """上传作业"""
        try:
            e1 = self.find(self.new_submit_btn1_locator)
            e1.click()
            e2 = self.find(self.sure_btn_locator)
            e2.click()
        except Exception as err:
            logging.error(f"点击更新提交失败：{err}")
        e3 = self.find(self.add_files_btn_locator)
        e3.send_keys(file_path)
        return self

    def delete_file(self):
        """删除文件"""
        e = self.find(self.delete_file_btn_locator)
        e.click()
        return self

    def click_submit_files(self):
        """点击作业提交"""
        time.sleep(2)
        try:
            self.click_element(self.new_submit_btn2_locator)
        except Exception as err:
            logging.error(f"点击更新提交失败：{err}")
            self.click_element(self.submit_btn_locator)
        return self

    def get_success_message(self):
        """获取作业成功提交信息"""
        e = self.find(self.success_message_locator)
        return e.text

    def click_known(self):
        """点击知道了"""
        e = self.find(self.known_locator)
        e.click()
        return self

    def comment(self, message):
        """作业留言"""
        message_elem = self.find(self.message_btn_locator)
        message_elem.click()
        input_elem = self.clear_input_box(self.comment_locator)
        input_elem.send_keys(message)
        self.click_element(self.save_btn_locator)
        return self

    def get_comment(self):
        """获取留言信息"""
        e = self.find(self.message_btn_locator)
        return e.text

    def view_status(self):
        """查看提交日志"""
        e = self.find(self.view_status_locator)
        e.click()
        log_elem = self.find(self.log_locator)
        return log_elem.text
