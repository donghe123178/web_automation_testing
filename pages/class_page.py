from selenium.webdriver.common.by import By
from common.base_page import BasePage
from pages.students_page import StudentsPage
from pages.homework_page import HomeWorkPage
# from pages.main_page import MainPage


class ClassPage(BasePage):
    """课堂页面操作：
        1.定位同学，点击，跳转至students页面
        2.定位作业，点击，定位作业标题，点击，跳转至homework页面
        3.获取课程码：定位课程码
        4.定位课堂，点击，回到main主页
    """
    classmates_locator = (By.XPATH, '//li[@class="li5"]//a')
    homework_locator = (By.XPATH, '//a[text()="作业"]')
    homework_title_locator = (By.XPATH, '//h3[@class="work-title "]//a')
    class_btn_locator = (By.XPATH, '//p//a')
    course_code_locator = (By.XPATH, '(//div[contains(@class,"codetip")])[3]')

    def click_classmates(self):
        """点击同学"""
        e = self.find(self.classmates_locator)
        e.click()
        return StudentsPage(self.driver)

    def click_upload_homework(self):
        """点击作业-上传作业"""
        e1 = self.find(self.homework_locator)
        e1.click()
        e2 = self.find(self.homework_title_locator)
        e2.click()
        return HomeWorkPage(self.driver)

    # def click_class_btn(self):
    #     """点击课堂，跳转至主页"""
    #     e = self.find(self.class_btn_locator)
    #     e.click()
    #     return MainPage(self.driver)

    def get_course_code(self):
        """获取课程码"""
        e = self.find(self.course_code_locator)
        return e.text
