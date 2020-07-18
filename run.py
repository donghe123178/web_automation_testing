"""
收集和运行用例
"""

import os
import pytest
from config.config import REPORTS_PATH

REPORT_FILE = os.path.join(REPORTS_PATH, "test_all")

if __name__ == '__main__':
    # pytest.main(["-m smoke", f"--html={REPORT_FILE}"])
    # pytest.main([f"--html={REPORT_FILE}"])
    # pytest.main(['--alluredir=reports/', "-m", "success"])
    pytest.main([f'--alluredir={REPORT_FILE}'])
    # 命令行allure运行
    # pytest - -alluredir = reports\test_all
    # 查看sllure报告
    # allure serve reports\test_all