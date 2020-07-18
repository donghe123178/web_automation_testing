from config import config
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class LoginPage(BasePage):
    """登录页面操作：
        1. 刷新登录页面
        2. 登录操作：定位用户名、输入手机号、定位密码、输入密码、定位登录、点击提交
        3. 获取返回的信息
    """
    url = config.HOST + "/User/login.html"

    phone_locator = (By.NAME, "account")
    pwd_locator = (By.NAME, "pass")
    login_btn_locator = (By.XPATH, '//a[contains(@class, "btn-btn")]')
    error_msg_locator = (By.XPATH, '//p[@class="error-tips"]')

    def get(self):
        """访问login页面"""
        self.driver.get(self.url)
        return self

    def login(self, mobile, pwd):
        """登录操作"""
        username_elem = self.find(self.phone_locator)
        username_elem.send_keys(mobile)
        pwd_elem = self.find(self.pwd_locator)
        pwd_elem.send_keys(pwd)
        self.click_element(self.login_btn_locator)
        return self

    def get_error_msg(self):
        """获取错误信息"""
        e = self.find(self.error_msg_locator)
        return e.text
