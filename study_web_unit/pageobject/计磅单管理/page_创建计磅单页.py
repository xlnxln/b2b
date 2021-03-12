from pageobject.首页.page_obj_首页 import HomePage
from pagelocators.计磅单管理.page_loc_创建计磅单 import CreateJiBang as loc
from common.handle_logger import logger


class CreateJiBangPage(HomePage):

    # 输入订单编号
    def input_order_id(self, order_id):
        logger.info("--- 输入订单编号 ： {} ---".format(order_id))
        self.find_element(loc.order_id_loc).send_keys(order_id)

    # 选择采购经理人
    def select_linker(self, tel):
        logger.info("--- 点击采购经理人手机号输入框 ---")
        self.find_element(loc.linker_loc).click()
        # 获取所有采购经理人的手机号
        tels = self.find_elements(loc.linker_tel_loc)
        # 判断要选择的采购经理人是否在列表中
        try:
            for i in tels:
                if i.text == tel:
                    i.click()
                    logger.info("--- 选择采购经理人 ： {} ---".format(tel))
                    break

            logger.info("--- 选择采购经理人后点击确定 ---")
            self.find_element(loc.linker_yes_loc).click()
            try:
                # 判断有没有错误提示信息
                self.wait_ele_visible(loc.linker_err_msg_loc, visible=None)
            except:
                logger.exception("--- 提示信息：请选择采购经理人 ---")
                raise
            else:
                logger.info("--- 选择采购经理人成功 ---")
        except:
            logger.info("--- 错误信息：选择的采购经理人不存在 ---")

    # 选择收款账户
    def select_bank_card(self, bank_card_id):
        logger.info("--- 点击收款账户输入框 ---")
        self.find_element(loc.bank_card_loc).click()
        # 获取所有收款账户的姓名
        name = self.find_elements(loc.bank_card_name_loc)
        # 获取所有收款账户的银行卡
        card = self.find_elements(loc.bank_card_id_loc)

        try:
            for i in range(len(card)):
                # 判断要选择的收款账户银行卡是否在列表中
                logger.info("--- 查找收款银行卡号 ： {} ---".format(bank_card_id))
                if card[i].text == bank_card_id:
                    logger.info("--- 查找收款银行卡号 ： {} 成功---".format(bank_card_id))
                    self.find_element(loc.bank_card_select_button(i+1)).click()
                    logger.info("--- 查找收款账户成功 ---")
                    break

            logger.info("--- 选择收款账户后点击确定 ---")
            self.find_element(loc.bank_card_yes_loc).click()

            try:
                # 判断有没有错误提示信息
                self.wait_ele_visible(loc.bank_card_err_msg_loc, visible=None)
            except:
                logger.exception("--- 提示信息：请选择收款账户 ---")
                raise
            else:
                logger.info("--- 选择收款账户成功 ---")
        except:
            logger.exception("--- 选择的收款账户银行卡不存在 ---")

    # 输入车牌号
    def input_car_num(self, car_num):
        logger.info("--- 输入车牌号 ： {} ---".format(car_num))
        self.find_element(loc.car_num_loc).send_keys(car_num)

    # 输入毛重
    def input_mao_weight(self, mao_weight):
        logger.info("--- 输入毛重 ： {} ---".format(mao_weight))
        self.find_element(loc.mao_weight_loc).send_keys(mao_weight)

    # 输入皮重
    def input_pi_weight(self, pi_weight):
        logger.info("--- 输入皮重 ： {} ---".format(pi_weight))
        self.find_element(loc.pi_weight_loc).send_keys(pi_weight)

    # 输入扣重
    def input_kou_weight(self, kou_weight):
        logger.info("--- 输入扣重 ： {} ---".format(kou_weight))
        self.find_element(loc.kou_weight_loc).send_keys(kou_weight)

    # 输入毛重称重时间
    def input_mao_date(self, mao_date):
        logger.info("--- 输入毛重称重时间 ： {} ---".format(mao_date))
        self.find_element(loc.mao_date_loc).send_keys(mao_date)

    # 输入皮重称重时间
    def input_pi_date(self, pi_date):
        logger.info("--- 输入皮重称重时间 ： {} ---".format(pi_date))
        self.find_element(loc.pi_date_loc).send_keys(pi_date)

    # 输入毛重司磅员
    def input_mao_sibangyuan(self, mao_sibangyuan):
        logger.info("--- 输入毛重司磅员 ： {} ---".format(mao_sibangyuan))
        self.find_element(loc.mao_sibangyuan_loc).send_keys(mao_sibangyuan)

    # 输入皮重司磅员
    def input_pi_sibangyuan(self, pi_sibangyuan):
        logger.info("--- 输入皮重司磅员 ： {} ---".format(pi_sibangyuan))
        self.find_element(loc.pi_sibangyuan_loc).send_keys(pi_sibangyuan)

    # 上传计磅单图片
    # def input_jibangdan_img(self, jibangdan_img_path):
    #     logger.info("--- 上传计磅单图片 ---")
    #     # self.find_element(loc.jibangdan_img_loc).click()
    #     # self.find_element(loc.jibangdan_img_loc).send_keys(jibangdan_img_path)
    #     self.driver.find_element_by_xpath(loc.jibangdan_img_loc).send_keys(jibangdan_img_path)