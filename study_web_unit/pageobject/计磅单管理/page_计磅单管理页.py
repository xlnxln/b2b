from pageobject.首页.page_obj_首页 import HomePage
from common.handle_logger import logger
from pagelocators.计磅单管理.page_loc_计磅单管理 import JiBangPage as loc


class JiBangPage(HomePage):

    def __click_tab_uncomplete(self):
        logger.info("--- 点击未完成标签页 ---")
        self.find_element(loc.uncomplete_loc).click()

    def click_create(self):
        self.__click_tab_uncomplete()
        logger.info("--- 点击创建 ---")
        self.find_element(loc.create_loc).click()