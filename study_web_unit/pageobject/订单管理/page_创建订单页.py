from pageobject.订单管理.page_订单管理页 import OrderPage
from pagelocators.订单管理.page_loc_创建订单页 import OrderCreatePageLoc as loc
from common.handle_logger import logger


class OrderCreatePage(OrderPage):
    """创建订单页面"""

    # 选择采购类别
    def select_kind(self, kind):
        logger.info("--- 选择采购类别：{} ---".format(kind))
        # 获取所有采购类别的名字
        kinds = self.find_elements(loc.kind_loc)
        try:
            # 判断想选择的采购类别是否在列表中，存在时点击选择
            for i in kinds:
                if i.text == kind:
                    i.click()
                    break
        except:
            logger.exception("--- 错误信息：选择的采购类别不存在 ---")

    # 选择生产企业
    def select_manu(self, manu_name):
        logger.info("--- 选择生产企业：{} ---".format(manu_name))
        # 点击生产企业选择框
        self.find_element(loc.manu_loc).click()
        # 获取所有生产企业的名字
        names = self.find_elements(loc.manu_name_loc)
        try:
            # 判断想选择的生产企业是否在列表中，存在时点击选择
            for i in names:
                if i.text == manu_name:
                    i.click()
                    break

            logger.info("--- 选择生产企业后，点击确定 ---")
            # 选择生产企业后点击确定
            self.find_element(loc.manu_yes_loc).click()
            try:
                # 判断是否有错误信息提示框
                self.wait_ele_visible(loc.manu_msg_loc, visible=None)
            except:
                logger.exception("--- 提示信息：请选择生产企业 ---")
                raise
            else:
                logger.info("--- 选择生产企业成功 ---")
        except:
            logger.exception("--- 错误信息：选择的生产企业不存在 ---")

    # 输入详细地址
    def input_address(self, address=None):
        # 判断详细地址输入框是否为空，为空时输入信息
        if self.find_element(loc.address_loc).get_attribute("value"):
            pass
        else:
            logger.info("--- 输入详细地址：{} ---".format(address))
            self.find_element(loc.address_loc).send_keys(address)

    # 选择料型
    def select_product(self):
        # 选择料型-板料-冲子料
        logger.info("--- 选择料型 ---")
        self.find_element(loc.product_loc).click()
        logger.info("--- 选择板料 ---")
        self.find_element(loc.product_name_loc).click()
        logger.info("--- 选择一级 ---")
        self.find_element(loc.product_name1_loc).click()

    # 输入规格
    def input_size(self, size):
        logger.info("--- 输入规格：{} ---".format(size))
        self.find_element(loc.size_loc).send_keys(size)

    # 输入销售单价
    def input_sale_unit_price(self, sale_unit_price):
        logger.info("--- 输入销售单价：{} ---".format(sale_unit_price))
        self.find_element(loc.sale_unit_price_loc).send_keys(sale_unit_price)

    # 输入采购单价
    def input_purchase_unit_price(self, purchase_unit_price):
        logger.info("--- 输入采购单价：{} ---".format(purchase_unit_price))
        self.find_element(loc.purchase_unit_price_loc).send_keys(purchase_unit_price)

    # 输入采购数量
    def input_purchase_amount(self, purchase_amount):
        logger.info("--- 输入采购数量：{} ---".format(purchase_amount))
        self.find_element(loc.purchase_amount_loc).send_keys(purchase_amount)

    # 输入结算周期
    def input_settle_cycle(self, settle_cycle):
        logger.info("--- 输入结算周期：{} ---".format(settle_cycle))
        self.find_element(loc.settle_cycle_loc).send_keys(settle_cycle)

    # 输入采购开始时间
    def input_begin_time(self, begin_time):
        logger.info("--- 输入采购开始时间 ： {} ---".format(begin_time))
        self.find_element(loc.begin_time_loc).clear()
        self.find_element(loc.begin_time_loc).send_keys(begin_time)

    # 输入才否截止时间
    def input_end_time(self, end_time):
        logger.info("--- 输入采购截止时间 ： {} ---".format(end_time))
        self.find_element(loc.end_time_loc).clear()
        self.find_element(loc.end_time_loc).send_keys(end_time)

    # 设置对供货商可见
    def select_supply_user_yes(self):
        logger.info("--- 设置对供货商可见 ---")
        self.find_element(loc.supply_user_yes).click()

    # 输入说明
    def input_desc(self, desc):
        logger.info("--- 输入说明：{} ---".format(desc))
        self.find_element(loc.desc_loc).send_keys(desc)

    # 选择采购经理人
    def select_linker(self, linker_name):
        logger.info("--- 选择采购经理人：{} ---".format(linker_name))
        # 点击选择按钮
        self.find_element(loc.linker_loc).click()
        # 获取所有采购经理人的名字
        names = self.find_elements(loc.linker_name_loc)
        try:
            # 判断想选择的采购经理人是否在列表中，存在时点击选择
            for i in names:
                if i.text == linker_name:
                    i.click()
                    break

            logger.info("--- 选择采购经理人后，点击确定 ---")
            self.find_element(loc.select_linker_yes_loc).click()
            try:
                # 判断是否有错误信息提示框
                self.wait_ele_visible(loc.linker_msg_loc, visible=None)
            except:
                logger.exception("--- 提示信息：请选择采购经理人 ---")
                raise
            else:
                logger.info("--- 选择采购经理人成功 ---")
        except:
            logger.info("--- 错误信息：选择的采购经理人不存在 ---")

    # 提交订单
    def submit_click(self):
        logger.info("--- 点击提交订单 ---")
        self.find_element(loc.submit_loc).click()
        logger.info("--- 提交订单成功 ---")

    def create_order(self, kind, manu_name, address, size, sale_unit_price, purchase_unit_price, purchase_amount
                     , settle_cycle, begin_time, end_time, linker_name, desc):
        """
        创建订单整体流程
        :param kind: 类别
        :param manu_name: 生产企业名称
        :param address: 详细地址
        :param size: 规格描述
        :param sale_unit_price: 销售单价
        :param purchase_unit_price: 采购单价
        :param purchase_amount: 采购数量
        :param settle_cycle: 结算周期
        :param begin_time: 开始时间
        :param end_time: 截止时间
        :param linker_name: 采购经理人
        :param desc: 说明
        """
        # 选择定价
        self.select_kind(kind)
        # 选择生产企业
        self.select_manu(manu_name)
        # 没有详细地址时输入
        self.input_address(address)
        # 选择品名（选了一个固定的）
        self.select_product()
        # 输入规格
        self.input_size(size)
        # 输入销售单价
        self.input_sale_unit_price(sale_unit_price)
        # 输入预采单价
        self.input_purchase_unit_price(purchase_unit_price)
        # 输入预采数量
        self.input_purchase_amount(purchase_amount)
        # 输入结算周期
        self.input_settle_cycle(settle_cycle)
        # 输入开始日期和时间
        self.input_begin_time(begin_time)
        # 输入截止时间和日期
        self.input_end_time(end_time)
        # 对供货商可见
        self.select_supply_user_yes()
        # 选择采购经理人
        self.select_linker(linker_name)
        # 输入说明
        self.input_desc(desc)
        # 点击提交
        self.submit_click()