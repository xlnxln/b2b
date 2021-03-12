from selenium.webdriver.common.by import By
from pageobject.basepage import BasePage
from time import sleep
from PIL import Image, ImageEnhance
import pytesseract


class LoginPage(BasePage):
    # 登录用户名
    username = (By.XPATH, '//input[@name="telephone"]')
    # 登录密码
    password = (By.XPATH, '//input[@name="password"]')
    # 登录验证码输入框
    code_input = (By.XPATH, '//input[@name="verification"]')
    # 登录按钮
    login_button = (By.XPATH, '//span[contains(text(),"立即登录")]/parent::button')
    # 验证码的图片
    code_img = (By.XPATH, '//div[@class="divIdentifyingCode"]//img')

    # 浏览器截图路径
    imgPath = 'E:/XLN_WorkSpace/study_web/code_img.png'

    def __init__(self, driver, url):
        super().__init__(driver)
        self.open_url(url)

    def remove(self, string):
        '''字符串去除空格'''

        return string.replace(" ", "")

    def getCodeImg(self):
        '''获取验证码图片'''

        # 验证码图片的元素定位
        img_el = self.driver.find_element(*self.code_img)
        # 获取整个浏览器的size
        chromeSize = self.driver.get_window_size()
        print("页面的总size:" + str(chromeSize))
        # 页面的总size:{'width': 1202, 'height': 1129}

        # 获取验证码图片的坐标
        self.location = img_el.location
        print("验证码图片坐标点:" + str(self.location))
        # 页面坐标点的size:{'x': 959, 'y': 518} x:指的图片左边距；y:指的图片上边距

        # 获取验证码图片的大小
        imgSize = img_el.size
        print("验证码的size:" + str(imgSize))
        # 验证码的size:{'height': 28, 'width': 70}

        # 左边距占整个浏览器的百分比
        left = self.location['x'] / chromeSize['width']
        # 上边距占整个浏览器的百分比
        top = self.location['y'] / chromeSize['height']
        # 右边距占整个浏览器的百分比
        right = (self.location['x'] + imgSize['width']) / chromeSize['width']
        # 下边距占整个浏览器的百分比
        bottom = (self.location['y'] + imgSize['height']) / chromeSize['height']
        print(left, top, right, bottom)
        # 0.7978369384359401 0.4588131089459699 0.8560732113144759 0.48361381753764393

        # 浏览器截屏操作
        self.driver.get_screenshot_as_file(self.imgPath)
        sleep(5)
        screenshotImgSize = Image.open(self.imgPath).size
        print("截图的size:" + str(screenshotImgSize))
        # 截图的size:(2404, 1950)    宽：2404，高：1950

        sleep(2)
        # 从文件读取截图，截取验证码位置再次保存
        img = Image.open(self.imgPath).crop((
            # left*screenshotImgSize[0],
            # top*screenshotImgSize[1]+100,
            # right*screenshotImgSize[0]+20,
            # bottom*screenshotImgSize[1]+150

            # 左边距百分比*截图的高≈截图左边距，再加上微调的距离+350
            left * screenshotImgSize[1] + 350,
            # 上边距百分比*截图的宽≈截图上边距，再加上微调的距离-100
            top * screenshotImgSize[0] - 100,
            # 右边距百分比*截图的高≈截图右边距，再加上微调的距离+400
            right * screenshotImgSize[1] + 400,
            # 下边距百分比*截图的宽≈截图下边距，再加上微调的距离-50
            bottom * screenshotImgSize[0] - 50
        ))
        img = img.convert('L')  # 转换模式：L | RGB
        img = ImageEnhance.Contrast(img)  # 增强对比度
        img = img.enhance(2.0)  # 增加饱和度
        img.save(self.imgPath)  # 再次保存图片
        sleep(5)

    def getCode(self):
        '''获取图片的code'''

        # 再次读取识别验证码
        img = Image.open('E:/XLN_WorkSpace/study_web/code_img.png')
        sleep(5)
        code = pytesseract.image_to_string(img).strip()
        print("=============输出的验证码为：" + self.remove(code))
        return code

    def loopGetCode(self):
        '''循环判断获取正确的图片code'''
        self.getCodeImg()
        code = self.remove(self.getCode())
        # 循环前获取code字数
        codeNumBf = len(code)

        # 如果获取图片的code值为空或者不满足4位数进行循环
        while (code == "") | (codeNumBf != 4):

            # 重新获取验证码
            self.driver.find_element(*self.code_img).click()
            self.getCodeImg()  # 获取验证码图片
            code = self.remove(self.getCode())
            # 循环后获取code字数
            codeNumAf = len(code)
            if code == "":
                print("code获取为空值=================")
                continue
            elif codeNumAf != 4:
                print("code获取不是4位数字=============")
                continue
            else:
                print("识别成功！")
            # 识别成功退出循环
            break
        print("=============输出的验证码为：" + code)
        # 输出满足条件的code
        return code

    def login(self, user, pwd):
        self.wait_for_time(self.login_button)
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.code_input).send_keys(self.loopGetCode())
        sleep(5)
        self.driver.find_element(*self.login_button).click()


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
