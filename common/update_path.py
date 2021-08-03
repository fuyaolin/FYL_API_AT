from pathlib import Path
from common.read_path import TESTCASE_YAML_PATH
import os


def update_path():
    PATH = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "testcase_path.py"
    f = open(PATH, 'w', encoding="utf-8")

    # 遍历testcase_yaml文件下所有的yaml文件路径
    path_lis = []
    for p in Path(TESTCASE_YAML_PATH).iterdir():
        path_lis.append(str(p))
        for s in p.rglob('*.yaml'):
            path_lis.append(str(s))

    f.write('\n"""测试用例路径"""\n\n')
    f.write('from common.read_path import BASE_PATH\n')
    f.write('import os\n\n\n')

    # 把测试用例路径写如read_path文件中
    for i in range(len(path_lis)):
        if path_lis[i].endswith(".yaml"):
            temp = path_lis[i].split("\\")[3:]
            PATH = ''
            for j in temp:
                PATH = PATH + " + os.path.sep + "
                PATH = PATH + "'" + j + "'"
            f.write("TESTCASE_YAML_" + str(temp[-1]).split('.')[0].upper() + "_PATH = BASE_PATH + " + "os.path.sep + " + "'testcase_yaml'" + PATH)
            f.write('\n')

    f.close()