from selenium.webdriver.common.by import By

"""创建订单页面元素定位"""


class OrderCreatePageLoc:

    # 类别
    kind_loc = (By.XPATH, '//span/parent::label')
    # 生产企业选择框
    manu_loc = (By.XPATH, '//div[@class="zhe"]')
    # 选择生产企业弹窗--所有生产企业的名字
    manu_name_loc = (By.XPATH, '//tbody//tr/td[2]/div')
    # 选择生产企业弹窗--确定按钮
    manu_yes_loc = (
    By.XPATH, '//span[text()="选择生产企业"]/parent::div/following-sibling::div//span[text()="确 定"]/parent::button')
    # 未选择生产企业的提示信息
    manu_msg_loc = (By.XPATH, '//p[text()="请选择生产企业"]')
    # 详细地址输入框
    address_loc = (By.XPATH, '//span[contains(text(),"地址")]/following-sibling::div/input')
    # 料型选择框
    product_loc = (By.XPATH, '//span[contains(text(),"料型")]/following-sibling::div//input')
    # 料型--板料
    product_name_loc = (By.XPATH, '//span[text()="板料"]')
    # 料型--一级
    product_name1_loc = (By.XPATH, '//span[text()="一级"]')
    # 规格输入框
    size_loc = (By.XPATH, '//span[contains(text(),"规格")]/following-sibling::div/input')
    # 销售单价输入框
    sale_unit_price_loc = (By.XPATH, '//span[contains(text(),"销售单价")]/following-sibling::div/input')
    # 采购单价输入框
    purchase_unit_price_loc = (By.XPATH, '//span[contains(text(),"采购单价")]/following-sibling::div/input')
    # 采购数量输入框
    purchase_amount_loc = (By.XPATH, '//span[contains(text(),"采购数量")]/following-sibling::div/input')
    # 结算周期输入框
    settle_cycle_loc = (By.XPATH, '//span[contains(text(),"结算周期")]/following-sibling::div/input')
    # 发布时间
    begin_time_loc = (By.XPATH, '//span[contains(text(),"发布时间")]/following-sibling::div/input')
    # 截止时间选择框
    end_time_loc = (By.XPATH, '//span[contains(text(),"截止时间")]/following-sibling::div/input')
    # 供货商可见
    supply_user_yes = (By.XPATH, '//span[contains(text(),"供货商可见")]/following-sibling::div//span[contains(text(),"是")]')
    # 说明输入框
    desc_loc = (By.XPATH, '//span[contains(text(),"说明")]/following-sibling::div/input')
    # 采购经理人选择按钮
    linker_loc = (By.XPATH, '//div[@class="row el-row"]//span[contains(text(),"采购经理人")]/following-sibling::button')
    # 选择采购经理人--所有采购经理人的名称
    linker_name_loc = (By.XPATH, '//span[text()="选择采购经理人"]/parent::div/following-sibling::div//table[@class="el-table__body"]//tr/td[2]/div')
    # 选择采购经理人--确定按钮
    select_linker_yes_loc = (
    By.XPATH, '//span[text()="选择采购经理人"]/parent::div/following-sibling::div//span[text()="确 定"]/parent::button')
    # 未选择采购经理人的提示信息
    linker_msg_loc = (By.XPATH, '//p[text()="请选择采购经理人"]')
    # 提交按钮
    submit_loc = (By.XPATH, '//span[text()="提交"]/parent::button')