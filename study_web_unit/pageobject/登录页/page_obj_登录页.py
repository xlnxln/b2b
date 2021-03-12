from time import sleep
from common.handle_logger import logger
from pagelocator.登录页.page_loc_登录页 import LoginPageLoc as loc
from pageobject.basepage import BasePage


class LoginPage(BasePage):
    """登录页面"""

    # def login(self, user, pwd):
    #     """识别图片验证码方式"""
    #
    #     # 输入用户名
    #     self.driver.find_element(*self.loc.username_loc).send_keys(user)
    #     # 输入密码
    #     self.driver.find_element(*self.password_loc).send_keys(pwd)
    #
    #     # 验证码图片的元素对象
    #     code_img_ele = self.driver.find_element(*self.code_img_loc)
    #     hc = HandleLoginVerifyCode(self.driver, code_img_ele)
    #     # 输入验证码
    #     self.driver.find_element(*self.code_input_loc).send_keys(hc.loopGetCode())
    #     # 点击登录按钮
    #     self.driver.find_element(*self.login_button_loc).click()
    #
    #     while True:
    #         # 判断当提示验证码错误时，重新获取验证码来登录
    #         try:
    #             # 获取提示框的提示信息
    #             code_err_msg = self.driver.find_element(*self.code_err_msg_loc).text
    #             if code_err_msg == "未查询到验证码信息" or code_err_msg == "验证码错误" or code_err_msg == "请输入验证码":
    #                 # 点击验证码图片更换验证码
    #                 self.driver.find_element(*self.code_img_loc).click()
    #                 # 清除验证码输入框的输入
    #                 self.driver.find_element(*self.code_input_loc).clear()
    #                 # 重新获取并输入验证码
    #                 self.driver.find_element(*self.code_input_loc).send_keys(hc.loopGetCode())
    #                 # 点击登录
    #                 self.driver.find_element(*self.login_button_loc).click()
    #         except:
    #             print("登录成功，进入首页")
    #             break


    # 输入用户名
    def input_username(self, username):
        logger.info("--- 输入登录用户名: {} ---".format(username))
        self.find_element(loc.username_loc).send_keys(username)

    # 输入密码
    def input_password(self, password):
        logger.info("--- 输入登录密码: {} ---".format(password))
        self.find_element(loc.password_loc).send_keys(password)

    # 手动输入验证码
    def input_verify_code(self):
        logger.info("--- 等待手动输入验证码 ---")
        sleep(10)

    # 点击登录
    def click_login(self):
        logger.info("--- 点击登录按钮 ---")
        self.find_element(loc.login_button_loc).click()

    # 登录流程
    def login(self, username, password):
        # 输入用户名
        self.input_username(username)
        # 输入密码
        self.input_password(password)
        # 输入验证码
        self.input_verify_code()
        # 点击登录
        self.click_login()