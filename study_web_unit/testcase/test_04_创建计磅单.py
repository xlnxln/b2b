import os
import unittest
from common.handle_logger import logger
from common.handle_filepath import testdata_dir
from common.handle_yaml import read_data
from testcase.login import Login
from pageobject.首页.page_obj_首页 import HomePage
from pageobject.计磅单管理.page_计磅单管理页 import JiBangPage
from pageobject.计磅单管理.page_创建计磅单页 import CreateJiBangPage
from selenium import webdriver

# 创建计磅单的测试数据
filepath = os.path.join(testdata_dir, "创建计磅单.yaml")
rd = read_data(filepath)["create_jibang"]


class CreateJiBang(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("========== 创建计磅单 测试用例开始执行 ==========")

    @classmethod
    def tearDownClass(cls):
        logger.info("========== 创建计磅单 测试用例执行结束 ==========")

    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        # 调用登录流程
        Login(self.driver)
        self.hp = HomePage(self.driver)  # 首页
        self.jp = JiBangPage(self.driver)  # 计磅单管理页
        self.cjp = CreateJiBangPage(self.driver)  # 创建计磅单页

    def tearDown(self):
        # 退出浏览器
        self.driver.close()
        self.driver.quit()

    @unittest.skip("无条件跳过用例")
    # 创建计磅单
    def test_create_jibang(self):
        # 进入计磅单管理
        self.hp.click_jibang()
        # 点击创建计磅单
        self.jp.click_create()
        # # 输入订单编号
        # self.cjp.input_order_id(rd["order_id"])
        # # 选择采购经理人
        # self.cjp.select_linker(rd["linker_tel"])
        # # 选择收款账户
        # self.cjp.select_bank_card(rd["bank_card_id"])
        # 上传计磅单图片
        # self.cjp.input_jibangdan_img(rd["jibangdan_img_path"])


if __name__ == '__main__':
    unittest.main()