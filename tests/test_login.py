import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.login_data import cases_error, cases_success


@pytest.mark.login
class TestLogin:
    @pytest.mark.smoke
    @pytest.mark.success
    @pytest.mark.parametrize("test_info", cases_success)
    def test_login_success(self, test_info, browser):
        """登录成功"""
        login_page = LoginPage(browser)
        login_page.get().login(test_info['mobile'], test_info['password'])
        user_info = MainPage(browser).get_user_account()
        try:
            assert test_info["expected"] in user_info, "登录成功"
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize("test_info", cases_error)
    def test_login_error(self, test_info, browser):
        """登录失败"""
        login_page = LoginPage(browser)
        login_page.get().login(test_info["mobile"], test_info["password"])
        error_msg = login_page.get_error_msg()
        try:
            assert test_info["expected"] == error_msg, "登录失败"
        except AssertionError as e:
            raise e

