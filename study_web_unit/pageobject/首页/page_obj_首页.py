from pageobject.登录页.page_obj_登录页 import LoginPage
from pagelocator.首页.page_loc_首页 import HomePageLoc as loc
from common.handle_logger import logger


class HomePage(LoginPage):
    """登录后的首页"""

    def click_user_info(self):
        # 点击账套信息按钮
        logger.info("--- 点击账套信息 ---")
        self.find_element(loc.user_info_loc).click()

    def is_user_exist(self):
        # 判断账套信息是否存在
        logger.info("--- 等待账套信息可见 ---")
        try:
            self.wait_ele_visible(loc.user_info_loc)
        except:
            logger.exception("--- 账套信息不可见 ---")
            return False
        else:
            logger.info("--- 账套信息可见 ---")
            return True

    def click_exit(self):
        # 点击退出按钮
        logger.info("--- 点击退出 ---")
        self.find_element(loc.exit_loc).click()

    def __click_supply_admin(self):
        # 点击供货管理
        logger.info("--- 点击供货管理 ---")
        self.find_element(loc.supply_admin_loc).click()

    def click_order(self):
        self.__click_supply_admin()
        # 点击订单管理
        logger.info("--- 点击订单管理 ---")
        self.find_element(loc.order_loc).click()
        logger.info("--- 进入订单管理页 ---")

    def click_supply(self):
        self.__click_supply_admin()
        # 点击供货单管理
        logger.info("--- 点击供货单管理 ---")
        self.find_element(loc.supply_loc)
        logger.info("--- 进入供货单管理页 ---")

    def __click_caigou_admin(self):
        logger.info("--- 点击采购管理 ---")
        self.find_element(loc.caigou_admin_loc).click()

    def click_jibang(self):
        self.__click_caigou_admin()
        logger.info("--- 点击计磅单管理 ---")
        self.find_element(loc.jibang_loc).click()
        logger.info("--- 进入计磅单管理页 ---")