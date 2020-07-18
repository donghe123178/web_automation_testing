"""
作业模块测试用例：
    1.提交作业
    2.作业留言
    3.查看作业提交情况
"""
import os
from config.config import FILES_PATH

cases_success = [
    {"file_path": FILES_PATH + r'\txt文档.txt',
     "message": "第1次提交作业！",
     "expected1": "作业提交成功",
     "expected2": "第1次提交作业！",
     "expected3": '添加了 "txt文档.txt" 并提交'},
    {"file_path": FILES_PATH + r'\txt文档.txt',
     "message": "第2次提交作业！",
     "expected1": "作业提交成功",
     "expected2": "第2次提交作业！",
     "expected3": '添加了 "txt文档.txt" 并提交'},
]


file_cases_success = [
    {"file_path": FILES_PATH + r'\png图片.png', "expected": "作业提交成功"},
    {"file_path": FILES_PATH + r'\py代码.py', "expected": "作业提交成功"},
    {"file_path": FILES_PATH + r'\txt文档.txt', "expected": "作业提交成功"},
    {"file_path": FILES_PATH + r'\xlsx文件.xlsx', "expected": "作业提交成功"},
    {"file_path": FILES_PATH + r'\压缩包.rar', "expected": "作业提交成功"},
]

if __name__ == '__main__':
    # F:\课堂派web自动化项目\files\png图片.png
    print(FILES_PATH)
    file_path = FILES_PATH + r'\压缩包.rar'
    print(file_path)
    print(os.path.join(FILES_PATH, "png图片.png"))
