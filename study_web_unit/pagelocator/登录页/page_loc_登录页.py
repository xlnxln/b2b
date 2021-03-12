from selenium.webdriver.common.by import By

"""登录页面元素定位"""


class LoginPageLoc:

    # 登录用户名
    username_loc = (By.XPATH, '//input[@name="telephone"]')
    # 登录密码
    password_loc = (By.XPATH, '//input[@name="password"]')
    # 登录验证码输入框
    code_input_loc = (By.XPATH, '//input[@name="verification"]')
    # 登录按钮
    login_button_loc = (By.XPATH, '//span[contains(text(),"立即登录")]/parent::button')
    # 验证码的图片
    code_img_loc = (By.XPATH, '//div[@class="divIdentifyingCode"]//img')
    # 验证码错误时的提示信息
    code_err_msg_loc = (By.XPATH, '//div[contains(@class,"el-message--error")]//p')