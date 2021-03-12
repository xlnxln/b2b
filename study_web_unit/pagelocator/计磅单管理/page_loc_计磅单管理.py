from selenium.webdriver.common.by import By

"""计磅单管理页面元素定位"""


class JiBangPage:

    # 未完成标签页
    uncomplete_loc = (By.XPATH, '//li[text()="未完成"]')
    # 创建
    create_loc = (By.XPATH, '//span[text()="创建"]/parent::button')