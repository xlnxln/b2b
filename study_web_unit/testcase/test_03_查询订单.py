import os
import unittest
from selenium import webdriver
from common.handle_logger import logger
from testcase.login import Login
from pageobject.首页.page_obj_首页 import HomePage
from pageobject.订单管理.page_订单管理页 import OrderPage
from common.handle_yaml import read_data
from common.handle_filepath import testdata_dir

# 查询订单的测试数据
filepath = os.path.join(testdata_dir, "data_查询订单.yaml")
rd = read_data(filepath)["select_order"]


class TestSelectOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("========== 查询订单 测试用例开始执行 ==========")

    @classmethod
    def tearDownClass(cls):
        logger.info("========== 查询订单 测试用例执行结束 ==========")

    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        # 调用登录流程
        Login(self.driver)
        self.hp = HomePage(self.driver)  # 首页
        self.op = OrderPage(self.driver)  # 订单管理页

    def tearDown(self):
        # 退出浏览器
        self.driver.close()
        self.driver.quit()

    def test_01_select_order_by_cauigou_id(self):
        logger.info("--- 输入采购编号查询 ---")
        # 点击供货管理--订单管理
        self.hp.click_order()
        # 输入采购编号
        self.op.input_caigou_id(rd["caigou_id"])
        # 点击查询
        self.op.click_select()
        # 断言
        try:
            self.assertTrue(self.op.result(rd["caigou_id"]))
            logger.info("--- 断言成功 ---")
        except:
            logger.exception("--- 断言失败 ---")

    def test_02_select_order_by_order_id(self):
        logger.info("--- 输入订单编号查询 ---")
        # 点击供货管理--订单管理
        self.hp.click_order()
        # 输入订单id
        self.op.input_order_id(rd["order_id"])
        # 点击查询
        self.op.click_select()
        # 断言
        try:
            self.assertTrue(self.op.result(rd["order_id"]))
            logger.info("--- 断言成功 ---")
        except:
            logger.exception("--- 断言失败 ---")


if __name__ == '__main__':
    unittest.main()