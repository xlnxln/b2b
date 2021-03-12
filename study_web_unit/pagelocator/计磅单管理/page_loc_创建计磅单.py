from selenium.webdriver.common.by import By

"""创建计磅单页面元素定位"""


class CreateJiBang:
    # 订单编号输入框
    order_id_loc = (By.XPATH, '//span[contains(text(),"订单编号")]/following-sibling::div/input')
    # 经理人输入框
    linker_loc = (By.XPATH, '//span[contains(text(),"经理人手机号")]/following-sibling::div')
    # 选择经理人--所有采购经理人的名字
    linker_name_loc = (By.XPATH, '//div[@aria-label="选择采购经理人"]//td[2]/div')
    # 选择采购经理人--所有采购经理人的手机号
    linker_tel_loc = (By.XPATH, '//div[@aria-label="选择采购经理人"]//td[3]/div')
    # 选择采购经理人--确定按钮
    linker_yes_loc = (By.XPATH, '//span[text()="确 定"]/parent::button')
    # 选择采购经理人--错误提示信息
    linker_err_msg_loc = (By.XPATH, '//p[text()="请选择采购经理人"]')
    # 收款账户输入框
    bank_card_loc = (By.XPATH, '//span[contains(text(),"收款账户")]/following-sibling::div')
    # 选择收款账户--所有收款账户名字
    bank_card_name_loc = (By.XPATH, '//div[@aria-label="选择收款账户"]//td[2]/div')
    # 选择收款账户--所有收款账户的收款银行卡
    bank_card_id_loc = (By.XPATH, '//div[@aria-label="选择收款账户"]//td[3]/div')

    # 选择收款账户--勾选按钮
    @staticmethod
    def bank_card_select_button(i):
        bank_card_select_path = '//div[@aria-label="选择收款账户"]//tr[{}]//td[1]/div'.format(i)
        bank_card_select_button_loc = (By.XPATH, bank_card_select_path)
        return bank_card_select_button_loc

    # 选择收款账户--错误提示信息
    bank_card_err_msg_loc = (By.XPATH, '//p[text()="请选择收款账户"]')
    # 选择收款账户--确定按钮
    bank_card_yes_loc = (By.XPATH, '//span[text()="确定"]/parent::button')
    # 车牌号输入框
    car_num_loc = (By.XPATH, '//input[@placeholder="请输入车牌"]')
    # 毛重输入框
    mao_weight_loc = (By.XPATH, '//input[@placeholder="请输入毛重"]')
    # 皮重输入框
    pi_weight_loc = (By.XPATH, '//input[@placeholder="请输入皮重"]')
    # 扣重输入框
    kou_weight_loc = (By.XPATH, '//input[@placeholder="请输入扣重"]')
    # 毛重称重时间
    mao_date_loc = (By.XPATH, '//input[@placeholder="请输入毛重称重时间"]')
    # 皮重称重时间
    pi_date_loc = (By.XPATH, '//input[@placeholder="请输入皮重称重时间"]')
    # 毛重司磅员
    mao_sibangyuan_loc = (By.XPATH, '//input[@placeholder="请输入毛重司磅员"]')
    # 皮重司磅员
    pi_sibangyuan_loc = (By.XPATH, '//input[@placeholder="请输入皮重司磅员"]')
    # 计磅单图片
    # jibangdan_img_loc = (By.XPATH, '//p[text()="计磅单"]/preceding-sibling::div//input')
    # # 车头图片
    # car_head_img_loc = (By.XPATH, '//p[text()="车头"]/preceding-sibling::div')
    # # 车身图片
    # car_body_img_loc = (By.XPATH, '//p[text()="车身"]/preceding-sibling::div')
    # # 车尾图片
    # car_tail_img_loc = (By.XPATH, '//p[text()="车尾"]/preceding-sibling::div')
    # 提交
    submit_loc = (By.XPATH, '//span[text()="提交"]/parent::button')