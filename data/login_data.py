"""
    课堂派登录测试用例
"""
cases_success = [
    {"mobile": "18740865632", "password": "python123", "expected": "东何"}
]

cases_error = [
    {"mobile": "", "password": "12", "expected": "账号不能为空"},
    {"mobile": "19244533103", "password": "", "expected": "密码不能为空"},
    {"mobile": "19244533103", "password": "zx", "expected": "密码有效长度是6到30个字符"},
    {"mobile": "19244533103", "password": "123456", "expected": "用户不存在"}
]

