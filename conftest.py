import pytest
from selenium import webdriver
from config import config
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.login_data import cases_success
from data.course_data import cases_success as join_cs


@pytest.fixture(scope="class")
def browser():
    """启动和关闭浏览器"""
    # 初始化浏览器
    driver = webdriver.Chrome()
    # 设置隐式等待
    driver.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
    # 浏览器页面最大化
    driver.maximize_window()
    # 返回一个浏览器对象
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def login_page(browser):
    """已登录"""
    login_page = LoginPage(browser)
    user_info = cases_success[0]
    login_page.get().login(user_info["mobile"], user_info["password"])
    yield browser


@pytest.fixture(scope="class")
def join_course(login_page):
    """已加入某课程"""
    main_page = MainPage(login_page)
    course_code_info = join_cs[0]
    main_page.get().input_class_code(course_code_info["course_code"]).sure_join_course()
    main_page.get()  # 刷新页面：如果已加入课程，刷新页面节约时间
    yield login_page


@pytest.fixture(scope="class")
def enter_students_page(join_course):
    """进入学生页面"""
    MainPage(join_course).enter_class().click_classmates()
    yield join_course


@pytest.fixture(scope="class")
def enter_homework_page(join_course):
    """进入homework页面"""
    MainPage(join_course).enter_class().click_upload_homework()
    yield join_course
