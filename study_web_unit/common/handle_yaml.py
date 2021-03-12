import yaml
import os


# 读取yaml类型的配置文件
def read_data(filepath):
    """
    读取yaml类型的配置文件
    :param filepath: yaml文件的路径
    :return: 返回读取到的数据
    """
    fs = open(filepath, "r", encoding="utf-8")
    return yaml.load(fs)


if __name__ == '__main__':
    filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "testdata", "data_登录.yaml")
    rd = read_data(filepath)
    print(rd["login"]["user"])