"""
    课堂派加入课堂测试用例
"""
cases_success = [
    {"add_class_code": "P69UVV", "expected": "加入课堂成功"}
]

cases_error = [
    {"add_class_code": "123", "expected": "加课验证码必须是6位字符"},
    {"add_class_code": "123456", "expected": "该加课码不存在或者已经失效"},
]

