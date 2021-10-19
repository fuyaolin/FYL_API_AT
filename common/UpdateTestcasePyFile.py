import os
import glob
from common.ReadPath import TESTCASE_PY_PATH, TESTCASE_YAML_PATH, TESTCASE_PY_TEMPLATE_PATH


class ExeFile(object):
    def __init__(self):
        self.TESTCASE_PY_PATH = TESTCASE_PY_PATH
        self.TESTCASE_YAML_PATH = TESTCASE_YAML_PATH
        self.TESTCASE_PY_TEMPLATE_PATH = TESTCASE_PY_TEMPLATE_PATH

    @staticmethod
    def getAllFiles(path, suffix):
        """
        :param path: 查找文件夹的路径
        :param suffix: 查找文件的后缀
        :return: 文件夹下所有的文件名称
        """
        files_name = []
        files_path = []
        for root, dirs, files in os.walk(path):
            files_path.append(root)
        for i in set(files_path):
            file_path = glob.glob(i + os.sep + "*." + suffix)
            for file_name in file_path:
                end_name = (os.path.relpath(file_name, path)).split(".")[0]
                files_name.append(end_name)
        return files_name

    # 比较文件夹下文件的不同
    def dirCompare(self):
        py_file = self.getAllFiles(self.TESTCASE_PY_PATH, suffix="py")
        yaml_file = self.getAllFiles(self.TESTCASE_YAML_PATH, suffix="yaml")
        # 根据yaml比较py，py缺少的补上
        for yaml_name in yaml_file:
            if yaml_name not in py_file:
                self.mkdir(yaml_name)

    # 创建的py文件创建
    def mkdir(self, yaml_name):
        py_path = os.path.join(self.TESTCASE_PY_PATH, yaml_name + ".py")
        if len(str(py_path).split("\\")) != 1:
            new_py_path = os.path.dirname(py_path)
            if os.path.exists(new_py_path) is False:
                os.mkdir(new_py_path)
        # 写入执行脚本
        try:
            old_str = '{}'
            new_str = str(py_path).split('\\')[-2]
            with open(self.TESTCASE_PY_TEMPLATE_PATH, "r") as f1, open(py_path, "w", encoding='utf-8') as f2:
                for line in f1:
                    if old_str in line:
                        line = line.replace(old_str, new_str)
                    f2.write(line)
            if os.path.relpath(py_path):
                print("文件创建成功")
        except Exception:
            raise Exception("文件创建失败:" + py_path)
        finally:
            f1.close()
            f2.close()


if __name__ == '__main__':
    ExeFile().dirCompare()

# # 复制执行脚本
# try:
#     copy_file = open(self.TESTCASE_PY_TEMPLATE_PATH, "r")
#     with open(py_path, "w", encoding='utf-8') as f:
#         s = copy_file.read()
#         f.write(s)
#         copy_file.close()
#     if os.path.relpath(py_path):
#         print("文件创建成功")
#     self.modify(py_path)
# except Exception:
#     raise Exception ("文件创建失败:" + py_path)
# finally:
#     f.close()
