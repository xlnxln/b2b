import os

# 根目录
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据目录
testdata_dir = os.path.join(basedir, "testdata")

# 测试用例目录
testcase_dir = os.path.join(basedir, "testcase")

# 测试报告路径
report_dir = os.path.join(basedir, "output", "report")

# 截图路径
screenshot_dir = os.path.join(basedir, "output", "screenshot")

# 日志目录
log_dir = os.path.join(basedir, "output", "log")