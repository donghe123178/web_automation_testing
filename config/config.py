"""
配置文件：
    存放常量
"""
import os

# 隐式等待时间
IMPLICTLY_WAIT_TIMEOUT = 20
# host
HOST = "https://www.ketangpai.com"
# 项目根地址
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报告地址
REPORTS_PATH = os.path.join(ROOT_PATH, "reports")
# image_path 保存截图的路径
IMAGE_PATH = os.path.join(REPORTS_PATH, "screeshots")
# 用于文件上传功能的文件地址
FILES_PATH = os.path.join(ROOT_PATH, "files")

if __name__ == '__main__':
    print(IMAGE_PATH)
