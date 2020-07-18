import pytest
from pages.homework_page import HomeWorkPage
from data.homework_data import cases_success, file_cases_success
import logging


@pytest.mark.homework
class TestHomework:
    """测试Homework页面的上传作业，作业留言，查看作业提交状态：
        前置条件：进入homework页面
        1.上传作业
        2.留言
        3.查看提交日志
    """
    @pytest.mark.smoke
    @pytest.mark.homework
    @pytest.mark.parametrize("test_info", cases_success)
    def test_homework_success(self, test_info, enter_homework_page):
        """作业提交、留言、查看提交日志"""
        driver = enter_homework_page
        homework_page = HomeWorkPage(driver)
        homework_page.get().upload_files(test_info["file_path"]).comment(test_info["message"]).click_submit_files()

        file_actual = homework_page.get_success_message()
        comment_actual = homework_page.click_known().get_comment()
        log_actual = homework_page.view_status()
        try:
            assert file_actual == test_info["expected1"], "作业提交成功"
            assert comment_actual == test_info["expected2"], "作业留言成功"
            assert test_info["expected3"] in log_actual, "查看作业提交日志成功"
        except AssertionError as e:
            raise e

    @pytest.mark.homework
    @pytest.mark.parametrize("test_info", file_cases_success)
    def test_upload_homework_success(self, test_info, enter_homework_page):
        """提交作业成功"""
        driver = enter_homework_page
        homework_page = HomeWorkPage(driver)
        homework_page.get().upload_files(test_info["file_path"])
        homework_page.click_submit_files()
        file_actual = homework_page.get_success_message()
        try:
            assert file_actual == test_info["expected"], "作业提交成功"
        except AssertionError as e:
            raise e

