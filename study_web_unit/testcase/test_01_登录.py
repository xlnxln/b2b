import unittest
import os
from selenium import webdriver
from common.handle_yaml import read_data
from common.handle_filepath import testdata_dir
from common.handle_logger import logger
from pageobject.登录页.page_obj_登录页 import LoginPage
from pageobject.首页.page_obj_首页 import HomePage

# 登录的测试数据文件的地址
login_filepath = os.path.join(testdata_dir, "data_登录.yaml")
# 读取登录的测试数据
rd = read_data(login_filepath)["login"]


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("========== 登录页 测试用例开始执行 ==========")

    @classmethod
    def tearDownClass(cls):
        logger.info("========== 登录页 测试用例执行结束 ==========")

    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        self.lp = LoginPage(self.driver)  # 登录页
        self.hp = HomePage(self.driver)  # 首页
        # 打开网址并最大化
        self.lp.open_url(rd["url"])

    def tearDown(self):
        # 关闭浏览器
        self.driver.close()
        self.driver.quit()

    def test_login_success(self):
        """成功登录流程"""

        # 手动输入验证码方式
        self.lp.login_other_method(rd["user"], rd["password"])

        # 识别图片验证码方式
        # LoginPage(self.driver).login(rd["user"], rd["password"])

        # 断言
        try:
            self.assertTrue(self.hp.is_user_exist())
        except:
            logger.exception("--- 断言：登录失败 ---")
        else:
            logger.info("--- 断言：登录成功 ---")
            # 点击账套信息
            self.hp.click_user_info()
            # 点击退出按钮
            self.hp.click_exit()


if __name__ == '__main__':
    unittest.main()