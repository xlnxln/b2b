import unittest
import os
from selenium import webdriver
from common.handle_filepath import testdata_dir
from common.handle_yaml import read_data
from testcase.login import Login
from common.handle_logger import logger
from pageobject.首页.page_obj_首页 import HomePage
from pageobject.订单管理.page_订单管理页 import OrderPage
from pageobject.订单管理.page_创建订单页 import OrderCreatePage

# 创建订单的测试数据文件地址
filepath = os.path.join(testdata_dir, "data_创建订单.yaml")
# 读取测试数据
rd = read_data(filepath)["create_order"]


class TestCreateOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("========== 创建订单 测试用例开始执行 ==========")

    @classmethod
    def tearDownClass(cls):
        logger.info("========== 创建订单 测试用例执行结束 ==========")

    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        # 登录页
        Login(self.driver)

    def tearDown(self):
        # 关闭浏览器
        self.driver.close()
        self.driver.quit()

    def test_create_order(self):
        """成功创建订单流程"""

        # 点击供货管理--订单管理
        HomePage(self.driver).click_order()
        # 点击创建
        OrderPage(self.driver).click_create_order()
        # 创建订单
        OrderCreatePage(self.driver).create_order(rd["kind"],
                                                  rd["manu_name"],
                                                  rd["address"],
                                                  rd["size"],
                                                  rd["sale_unit_price"],
                                                  rd["purchase_unit_price"],
                                                  rd["purchase_amount"],
                                                  rd["settle_cycle"],
                                                  rd["begin_time"],
                                                  rd["end_time"],
                                                  rd["linker_name"],
                                                  rd["desc"])


if __name__ == '__main__':
    unittest.main()