"""
   封装一个自己的日志收集器
"""
import logging
import os
import colorlog
from datetime import datetime
from common.handle_filepath import log_dir


class MyLogger(logging.Logger):

    def __init__(self, file=None):
        super().__init__("日志名称")

        # 设置输出日志颜色
        log_colors_config = {
            'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }

        # 设置输出到文件的日志内容格式
        file_fmt = "%(levelname)s %(name)s [%(asctime)s] %(filename)s -> line:%(lineno)d %(message)s"
        # 日志使用ideolog插件，levelname要放在首位
        file_formatter = logging.Formatter(file_fmt)
        # 设置输出到控制台的日志内容格式
        console_fmt = "%(log_color)s %(levelname)s %(name)s [%(asctime)s] %(filename)s -> line:%(lineno)d %(message)s"
        console_formatter = colorlog.ColoredFormatter(console_fmt, log_colors=log_colors_config)

        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(console_formatter)
        handle1.setLevel("INFO")  # 设置控制台的日志输出级别
        self.addHandler(handle1)

        # 文件渠道--file不为None时输入日志到文件
        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(file_formatter)
            self.addHandler(handle2)


# 定义输出日志文件名称的格式
now_time = datetime.now().strftime("%Y-%m-%d %H_%M_%S")
file_name = now_time + " " + "日志.log"
file_path = os.path.join(log_dir, file_name)


# 实例化日志对象，供其他文件直接调用
logger = MyLogger(file_path)


if __name__ == '__main__':
    logger.info("测试输出日志")
    try:
        a = 1
        b = 2
        if a == b:
            pass
        else:
            logger.exception("错误")
    except:
        raise
    logger.debug("debug日志")
    logger.warning("warning日志")
