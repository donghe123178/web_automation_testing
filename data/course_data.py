"""
课堂模块测试用例：
    1.加入课堂功能
    2.进入课堂功能
    2.退出课堂功能
"""
cases_success = [{"course_code": "P69UVV", "password": "python123",
                  "expected1": "加入课堂成功", "expected2": "P69UVV", "expected3": "课程退课成功"}]

join_cases_success = [
    {"course_code": "P69UVV", "password": "python123"}
]

join_cases_error = [
    {"course_code": "123", "expected": "加课验证码必须是6位字符"},
    {"course_code": "123456", "expected": "该加课码不存在或者已经失效"},
]

exit_cases_error = [
    {"password": "zxz", "expected": "密码错误"}
]
