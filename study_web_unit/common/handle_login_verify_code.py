from PIL import Image, ImageEnhance
import pytesseract
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep
from common.handle_logger import logger


class HandleLoginVerifyCode:

    # 浏览器截图路径
    imgPath = 'E:/XLN_WorkSpace/study_web_unit/code_img.png'
    imgPath_code = 'E:/XLN_WorkSpace/study_web_unit/save.png'

    def __init__(self, driver: WebDriver, img_el):
        self.driver = driver
        # 验证码图片的元素定位对象
        self.img_el = img_el

    def remove(self, string):
        """
        字符串去除空格
        """

        return string.replace(" ", "")

    def getCodeImg(self):
        """获取验证码图片"""

        # 获取验证码图片的坐标
        location = self.img_el.location
        # print("验证码图片坐标点:" + str(location))

        # 获取验证码图片的大小
        imgSize = self.img_el.size
        # print("验证码的size:" + str(imgSize))

        # 等待验证码图片可见后，浏览器截屏
        self.driver.get_screenshot_as_file(self.imgPath)
        sleep(2)

        # 写成我们需要截取的位置坐标
        rangle = (int(location['x']-10),
                  int(location['y']-10),
                  int(location['x'] + imgSize['width']+10),
                  int(location['y'] + imgSize['height']+10))

        # 从文件读取截图，截取验证码位置再次保存
        img = Image.open(self.imgPath).crop(rangle)
        img = img.convert('L')  # 转换模式：L | RGB
        img = ImageEnhance.Contrast(img)  # 增强对比度
        img = img.enhance(2.0)  # 增加饱和度
        img.save(self.imgPath_code)  # 再次保存图片
        sleep(2)

    def getCode(self):
        '''获取图片的code'''

        # 再次读取识别验证码
        img = Image.open(self.imgPath_code)
        sleep(2)
        code = pytesseract.image_to_string(img).strip()
        return code

    def loopGetCode(self):
        """
        循环判断获取正确的图片code
        :return: 返回识别出的验证码
        """
        self.getCodeImg()
        code = self.remove(self.getCode())
        # 循环前获取code字数
        codeNumBf = len(code)

        # 如果获取图片的code值为空或者不满足4位数进行循环
        while (code == "") or (codeNumBf != 4):

            # 重新获取验证码
            self.img_el.click()
            sleep(1)
            self.getCodeImg()  # 获取验证码图片
            code = self.remove(self.getCode())
            # 循环后获取code字数
            codeNumAf = len(code)
            if code == "":
                # print("code获取为空值=================")
                logger.info("验证码获取为空值")
                continue
            elif codeNumAf != 4:
                # print("code获取不是4位数字=============")
                logger.info("验证码获取不是4位数字")
                continue
            else:
                # print("识别code成功！")
                logger.info("验证码识别成功")
            # 识别成功退出循环
            break
        # print("=============输出的验证码为：" + code)
        logger.info("输出的验证码为：{}".format(code))
        # 输出满足条件的code
        return code
