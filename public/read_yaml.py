"""
    解读yaml文件--未完成
"""
import yaml

class YamlUtil(object):
    def __init__(self, yaml_file):
        """
        通过init方法把yaml文件传入到这个类
        :param yaml_file:
        """
        self.yaml_file = yaml_file

    # 读取yaml文件
    def read_yaml(self):
        """
        读取yaml，对yaml反序列化
        :return:
        """
        with open(self.yaml_file, encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value
