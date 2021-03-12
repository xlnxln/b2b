from selenium.webdriver.common.by import By

"""首页元素定位"""


class HomePageLoc:
    # 账套信息按钮
    user_info_loc = (By.XPATH, '//p[@class="right-menu-icon-left"]')
    # 退出按钮
    exit_loc = (By.XPATH, '//div[text()="退出"]')

    # 采购管理分类按钮
    caigou_admin_loc = (By.XPATH, '//span[text()="采购管理"]/parent::div')
    # 采购管理--计磅单管理
    jibang_loc = (By.XPATH, '//span[text()="计磅单管理"]/parent::li')

    # 供货管理分类按钮
    supply_admin_loc = (By.XPATH, '//span[text()="供货管理"]/parent::div')
    # 供货管理--订单管理按钮
    order_loc = (By.XPATH, '//span[text()="订单管理"]/parent::li')
    # 供货管理--供货单管理按钮
    supply_loc = (By.XPATH, '//span[text()="供货单管理"]/parent::li')