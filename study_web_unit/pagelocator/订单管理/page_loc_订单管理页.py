from selenium.webdriver.common.by import By

"""订单管理页面元素定位"""


class OrderPageLoc:

    # 创建订单按钮
    create_order_loc = (By.XPATH, '//span[text()="创建"]/parent::button')
    # 采购编号输入框
    caigou_id_loc = (By.XPATH, '//input[@placeholder="请输入采购编号"]')
    # 订单编号输入框
    order_id_loc = (By.XPATH, '//input[@placeholder="请输入订单编号"]')
    # 查询按钮
    select_loc = (By.XPATH, '//span[text()="查询"]/parent::button')

    # 查询结果
    result_loc = (By.XPATH, '//tr[@class="el-table__row"]//td//div')