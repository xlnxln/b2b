import os
from common.handle_yaml import read_data
from common.handle_filepath import testdata_dir
from common.handle_logger import logger
from pageobject.page_登录页 import LoginPage
from pageobject.首页.page_obj_首页 import HomePage

# 登录的测试数据文件的地址
login_filepath = os.path.join(testdata_dir, "data_登录.yaml")
# 读取登录的测试数据
rd = read_data(login_filepath)["login"]


class Login:
    """封装登录操作"""

    def __init__(self, driver):
        self.driver = driver
        lp = LoginPage(self.driver)  # 登录页
        hp = HomePage(self.driver)  # 首页
        # 打开网址
        lp.open_url(rd["url"])
        # 登录页
        lp.login_other_method(rd["user"], rd["password"])

        # 判断登录是否成功
        try:
            if hp.is_user_exist():
               logger.info("--- 登录成功，进入首页 ---")
        except:
            logger.exception("--- 登录失败 ---")


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    Login(driver)
    driver.close()
    driver.quit()