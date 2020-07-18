import pytest
from pages.students_page import StudentsPage
from data.send_message_data import cases_success


@pytest.mark.message
class TestSendMessage:
    """测试Students页面的同学私信功能：
        前置条件：进入students页面
        1.发送私信
        2.断言
    """
    @pytest.mark.smoke
    @pytest.mark.success
    @pytest.mark.parametrize("test_info", cases_success)
    def test_send_message_success(self, test_info, enter_students_page):
        driver = enter_students_page
        student_page = StudentsPage(driver)
        actual = student_page.get().send_message(test_info["message"])
        try:
            assert actual in test_info["expected"], "留言成功"
        except AssertionError as e:
            raise e




