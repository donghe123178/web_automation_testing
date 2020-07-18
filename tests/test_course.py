import pytest
from data.course_data import cases_success, join_cases_success, join_cases_error, exit_cases_error
from pages.main_page import MainPage


@pytest.mark.course
class TestCourse:
    @pytest.mark.smoke
    @pytest.mark.success
    @pytest.mark.parametrize("test_info", cases_success)
    def test_join_exit_success(self, test_info, login_page):
        """加课、进入课堂、退课成功"""
        driver = login_page
        main_page = MainPage(driver)
        join_actual = main_page.get().input_class_code(test_info["course_code"]). \
            sure_join_course().get_success_msg()
        # class_page = main_page.enter_class()
        # code_actual = class_page.get_course_code()
        # main_page = class_page.click_class_btn()
        exit_actual = main_page.get().click_more_btn().exit_course(test_info["password"]).get_success_msg()
        try:
            assert join_actual == test_info["expected1"], "加课成功"
            # assert code_actual == test_info["expected2"], "进入课堂成功"
            assert exit_actual == test_info["expected3"], "退课成功"
        except AssertionError as e:
            raise e

    @pytest.mark.success
    @pytest.mark.parametrize("test_info", join_cases_success)
    def test_add_success(self, test_info, login_page):
        """加课成功"""
        driver = login_page
        main_page = MainPage(driver)
        actual = main_page.get().input_class_code(test_info["course_code"]). \
            sure_join_course().get_success_msg()
        try:
            assert actual == test_info["expected"], "加课成功"
        except AssertionError as e:
            raise e

    @pytest.mark.error
    @pytest.mark.parametrize("test_info", join_cases_error)
    def test_add_success(self, test_info, login_page):
        """加课失败"""
        driver = login_page
        main_page = MainPage(driver)
        actual = main_page.get().input_class_code(test_info["course_code"]). \
            sure_join_course().get_error_msg()
        try:
            assert actual == test_info["expected"], "加课失败"
        except AssertionError as e:
            raise e

    @pytest.mark.error
    @pytest.mark.parametrize("test_info", exit_cases_error)
    def test_exit_error(self, test_info, join_course):
        """退课失败"""
        driver = join_course
        main_page = MainPage(driver)
        actual = main_page.get().click_more_btn().exit_course(test_info["password"]).get_error_msg()
        try:
            assert actual == test_info["expected"], "退课失败"
        except AssertionError as e:
            raise e
