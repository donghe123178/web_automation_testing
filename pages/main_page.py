from config import config
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from pages.class_page import ClassPage


class MainPage(BasePage):
    """主页页面操作：
        1. 刷新首页
        2. 输入加课码：定位加入课程，点击，定位加课验证码输入框，输入加课码
        3. 定位确定按钮，点击确定
        4. 定位取消按钮，点击取消
        5. 获取错误信息
        6. 获取成功信息
        7. 退课操作：定位更多，点击，定位退课，点击，定位登录密码输入框，输入密码，定位退课按钮，点击提交
        8. 进入班级操作：定位班级，点击跳转至class界面
        9. 获取用户账户信息：定位
    """
    url = config.HOST + "/Main/index.html"

    user_account_locator = (By.XPATH, '//img[@class="avatar"]')

    add_class_btn_locator = (By.XPATH, '//div[contains(@class, "ktcon1l")]')
    input_add_class_code_locator = (By.XPATH, '//div[@class="chuangjiankccon"]//input[@type="text"]')
    sure_btn_locator = (By.XPATH, '//li[@class="cjli2"]//a[contains(@class, "btn-positive")]')

    error_msg_locator = (By.XPATH, '//div[@id="error-tip"]//span')
    success_msg_locator = (By.XPATH, '//div[@id="show-tip"]//span')

    more_btn_locator = (By.XPATH, '//a[contains(@class, "kdmore")]//span')
    exit_class_btn_01_locator = (By.XPATH, '//li[contains(@class, "kdli3")]//a')
    cancel_btn_locator = (By.XPATH, '//li[@class="cjli1"]//a')
    input_pwd_locator = (By.XPATH, '//input[@type="password"]')
    exit_class_btn_02_locator = (By.XPATH, '//li[@class="dli2"]//a[contains(@class, "btn-positive")]')

    enter_class_locator = (By.XPATH, '//a[@class="jumptoclass"]')

    course_code_locator = (By.XPATH, '//p[contains(@class,"invitecode")]')

    def get(self):
        """访问首页"""
        self.driver.get(self.url)
        return self

    def input_class_code(self, class_code):
        """输入课程码"""
        self.click_element(self.add_class_btn_locator)
        e = self.wait_element_visible(self.input_add_class_code_locator)
        e.send_keys(class_code)
        return self

    def sure_join_course(self):
        """点击确定加入"""
        self.click_element(self.sure_btn_locator)
        return self

    def cancel_class(self):
        """取消加入课程操作"""
        e = self.find(self.cancel_btn_locator)
        e.click()
        return self

    def get_error_msg(self):
        """获取错误信息"""
        e = self.wait_element_visible(self.error_msg_locator)
        return e.text

    def get_success_msg(self):
        """获取成功信息"""
        e = self.wait_element_visible(self.success_msg_locator)
        return e.text

    def click_more_btn(self):
        """点击更多按钮"""
        e = self.find(self.more_btn_locator)
        e.click()
        return self

    def exit_course(self, password):
        """退出课程"""
        # 点击退课按钮
        e1 = self.find(self.exit_class_btn_01_locator)
        e1.click()
        # 输入密码
        e = self.wait_element_visible(self.input_pwd_locator)
        e.send_keys(password)
        # 点击退课按钮
        self.click_element(self.exit_class_btn_02_locator)
        return self

    def enter_class(self):
        """进入班级操作"""
        e = self.find(self.enter_class_locator)
        e.click()
        return ClassPage(self.driver)

    def get_user_account(self):
        """获取用户的账号信息"""
        e = self.find(self.user_account_locator)
        return e.get_attribute("title")

    def get_course_code(self):
        """获取课程码"""
        e = self.find(self.course_code_locator)
        return e.text
