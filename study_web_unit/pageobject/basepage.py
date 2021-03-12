import os
from time import sleep, strftime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from common.handle_filepath import screenshot_dir
from common.handle_logger import logger


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 打开网址
    def open_url(self, url):
        logger.info("打开网址：{}".format(url))
        self.driver.get(url)
        # 页面最大化
        self.driver.maximize_window()

    # 等待元素可见
    def wait_ele_visible(self, loc, visible=True):
        if visible:
            # visible为true时，执行元素是否可见的判断
            logger.info("等待元素：{} 是否可见".format(loc))
            try:
                wait = WebDriverWait(self.driver, 20, 0.5)
                wait.until(EC.visibility_of_element_located(loc))
                sleep(1)
            except:
                logger.exception("等待元素：{} 可见失败，元素当前不可见".format(loc))
                raise
            else:
                logger.info("等待元素：{} 可见成功，元素当前可见")
        else:
            # visible为false时，执行元素是否不可见的判断
            logger.info("等待元素：{} 是否不可见".format(loc))
            try:
                wait = WebDriverWait(self.driver, 20, 0.5)
                wait.until(EC.invisibility_of_element_located(loc))
                sleep(1)
            except:
                logger.exception("等待元素：{} 不可见失败，元素当前可见".format(loc))
                raise
            else:
                logger.info("等待元素：{} 不可见成功，元素当前不可见")

    # 查找一个元素
    def find_element(self, loc):
        # 先等待元素可见
        self.wait_ele_visible(loc)
        logger.info("查找元素：{}".format(loc))
        try:
            self.driver.find_element(*loc)
            return self.driver.find_element(*loc)
        except:
            logger.exception("元素查找失败，找不到该元素，开始截取当前页面图像".format(loc))
            self.save_screenshot()
            raise

    # 查找一组元素
    def find_elements(self, loc):
        # 先等待元素可见
        self.wait_ele_visible(loc)
        logger.info("查找元素：{}".format(loc))
        try:
            self.driver.find_element(*loc)
            return self.driver.find_elements(*loc)
        except:
            logger.exception("元素查找失败，找不到该元素，开始截取当前页面图像".format(loc))
            self.save_screenshot()
            raise

    # 截图
    def save_screenshot(self):
        current_time = strftime('%Y-%m-%d-%H-%M-%S')
        filepath = os.path.join(screenshot_dir, "{}.png".format(current_time))
        self.driver.save_screenshot(filepath)
        print("已截取当前页面，截图路径：{}".format(filepath))