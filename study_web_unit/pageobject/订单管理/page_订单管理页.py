from pagelocators.订单管理.page_loc_订单管理页 import OrderPageLoc as loc
from pageobject.page_登录页 import LoginPage
from common.handle_logger import logger


class OrderPage(LoginPage):
    """订单管理页面"""

    def click_create_order(self):
        # 点击创建订单
        logger.info("--- 点击创建订单按钮 ---")
        self.find_element(loc.create_order_loc).click()
        logger.info("--- 成功进入创建订单页面 ---")

    def input_caigou_id(self, caigou_id):
        logger.info("--- 输入采购编号 ---")
        self.find_element(loc.caigou_id_loc).clear()
        self.find_element(loc.caigou_id_loc).send_keys(caigou_id)

    def input_order_id(self, order_id):
        logger.info("--- 输入订单id ---")
        self.find_element(loc.order_id_loc).clear()
        self.find_element(loc.order_id_loc).send_keys(order_id)

    def click_select(self):
        logger.info("--- 点击查询 ---")
        self.find_element(loc.select_loc).click()

    def result(self, value):
        logger.info("--- 判断是否查询到结果 ---")
        # 定位到所有的查询结果
        all_result = self.find_elements(loc.result_loc)
        try:
            # 判断查询条件是否显示在查询结果中
            for i in all_result:
                if value == i.text:
                    logger.info("--- 查询到结果 ---")
                    return True
        except:
            logger.exception("--- 未查到结果 ---")
            return False
