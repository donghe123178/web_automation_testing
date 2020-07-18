"""
base_page
    页面对象有一些共同的基本操作，可以封装起来，并可以在基本操作当中，加上日志和截图的处理
    1.查找元素，都需要等待
    2.alert弹出框，窗口的切换
    3.鼠标操作
    4.上传文件
"""
import os
import logging
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from config.config import IMAGE_PATH
from datetime import datetime
from pywinauto import Desktop
import time


class BasePage:

    def __init__(self, driver: Chrome):  # 函数注解
        self.driver = driver

    def find(self, locator):
        """查找元素"""
        try:
            e = self.driver.find_element(*locator)
        except Exception as err:
            # 没有找到元素
            logging.error(f"元素定位失败：{err}")
            # 截图
            self.save_screenshot()
        else:
            return e

    def save_screenshot(self):
        """截图"""
        # 路径拼接
        # 时间戳命名，防止覆盖
        ts_str = datetime.now().strftime("%y-%m_%d-%H-%M-%S")
        file_name = os.path.join(IMAGE_PATH, ts_str) + '.png'
        self.driver.save_screenshot(file_name)
        return self

    def find_and_red(self, locator):
        """定位元素并标红,装饰器实现"""
        try:
            e = self.driver.find_element(*locator)
            js_code = "arguments[0].style.borderColor='red';"
            self.driver.execute_script(js_code, e)
        except Exception as err:
            logging.error(f"元素定位失败：{err}")
            self.save_screenshot()
        else:
            return e

    def wait_element_clickable(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素可以被点击"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.element_to_be_clickable(locator))
        except Exception as err:
            logging.error(f"元素定位失败：{err}")
            self.save_screenshot()
        else:
            return e

    def wait_element_visible(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素可见"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.visibility_of_element_located(locator))
        except Exception as err:
            logging.error(f"元素定位失败：{err}")
            self.save_screenshot()
        else:
            return e

    def wait_element_present(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素被加载"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.presence_of_element_located(locator))
        except Exception as err:
            logging.error(f"元素定位失败：{err}")
            self.save_screenshot()
        else:
            return e

    def click_element(self, locator):
        """点击某个元素"""
        e = self.wait_element_clickable(locator)
        e.click()
        return self

    def double_click(self, locator):
        """双击某个元素"""
        e = self.wait_element_clickable(locator)
        ac = ActionChains(self.driver)
        ac.double_click(e).perform()
        return self

    def move_to(self, locator):
        """鼠标悬停"""
        e = self.find(locator)
        ac = ActionChains(self.driver)
        ac.move_to_element(e).perform()
        return self

    def switch_to_frame(self, e, wait=False):
        """iframe切换，内嵌网页"""
        if not wait:
            self.driver.switch_to.frame(e)
            return self
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(e))
        return self

    def add_file(self, file_path):
        """添加文件"""
        app = Desktop()
        dialog = app['打开']
        time.sleep(2)
        dialog["Edit"].type_keys(file_path)
        dialog["Button"].click()

    def clear_input_box(self, locator):
        input_box = self.find(locator)
        try:
            input_box.clear()
        except Exception as err:
            logging.error(f"输入框清空失败：{err}")
        finally:
            return input_box


if __name__ == '__main__':
    pass
    # ts_str = datetime.now().strftime("%y-%m_%d-%H-%M-%S")
    # file_name = os.path.join(IMAGE_PATH, ts_str) + '.png'
    # print(file_name)
