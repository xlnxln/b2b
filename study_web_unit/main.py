import unittest
import os
from HTMLTestRunnerNew import HTMLTestRunner
from common.handle_filepath import testcase_dir, report_dir

# 收集测试用例
suite = unittest.TestLoader().discover(testcase_dir)

# 测试报告路径
report_file = os.path.join(report_dir, "report.html")

# 运行测试用例并生成测试报告
with open(report_file, "wb") as fs:
    runner = HTMLTestRunner(fs, title="B2B自动化测试报告",description="自己练习", tester="徐立楠")
    runner.run(suite)

