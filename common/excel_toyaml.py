"""
    excel表格数据转化为yaml文件
    默认为exel文件夹下所有问价
    可在common.read_path下修改EXCEL_PATH的读取路径
"""
import yaml
import os
import copy
from common.read_excel import ReadExcel
from common.read_path import TESTCASE_YAML_PATH


class DoExcel(ReadExcel):
    def __init__(self):
        super().__init__()
        self.json = {
                    "order_by": [],
                    "all_skip": "false",
                    "testcase": {}
                     }

    def excel_data(self):
        # 返回值是列表形式的
        sheet_data = DoExcel().read_excel_path()
        json_data = copy.deepcopy(self.json)
        for val in range(len(sheet_data)):
            if sheet_data[val] is not None:
                sheet = sheet_data[val][0]
                value = sheet_data[val][-1] if type(sheet_data[val][-1]) is not "dict" else eval(sheet_data[val][-1])
                if "filename" in value.keys() and value["filename"] is not None:
                    filename = value["filename"]
                else:
                    raise Exception("filename参数必须存在且不能为空")

                if "case" in value.keys() and value["case"] is not None:
                    case = value["case"]
                    json_data['testcase'][case] = {}
                else:
                    raise Exception("case参数必须存在且不能为空")

                if "skip" in value.keys() and value["skip"] is not None:
                    skip = value["skip"]
                    json_data['testcase'][case]['skip'] = skip
                else:
                    raise Exception("skip参数必须存在且不能为空")
                if "name" in value.keys() and value["name"] is not None:
                    name = value["name"]
                    json_data['testcase'][case]['name'] = name
                if "title" in value.keys() and value["title"] is not None:
                    title = value["title"]
                    json_data['testcase'][case]['title'] = title
                if "setup" in value.keys() and value["setup"] is not None:
                    setup = value["setup"]
                    json_data['testcase'][case]['setup'] = setup
                if "teardown" in value.keys() and value["teardown"] is not None:
                    teardown = value["teardown"]
                    json_data['testcase'][case]['teardown'] = teardown
                if "sleep" in value.keys() and value["sleep"] is not None:
                    sleep = value["sleep"]
                    json_data['testcase'][case]['sleep'] = sleep

                json_data['testcase'][case]['request'] = {}
                if "header" in value.keys() and value["header"] is not None:
                    header = value["header"]
                    json_data['testcase'][case]['request']['header'] = header
                if "url" in value.keys() and value["url"] is not None:
                    url = value["url"]
                    json_data['testcase'][case]['request']['url'] = url
                if "method" in value.keys() and value["method"] is not None:
                    method = value["method"]
                    json_data['testcase'][case]['request']['method'] = method
                if "body" in value.keys() and value["body"] is not None:
                    body = eval(value["body"])
                    json_data['testcase'][case]['request']['body'] = body

                json_data['testcase'][case]['check'] = []
                check = {}
                if ("check_value" and "check_code") in value.keys()\
                        and (value["check_value"] and value["check_code"]) is not None:
                    check_code = value["check_code"]
                    check_value = value["check_value"]
                    check[check_code] = [check_value]
                    json_data['testcase'][case]['check'].append(check)

                # 判断sheet页，调用函数，转换数据
                if val != len(sheet_data)-1:
                    if sheet == sheet_data[val+1][0]:
                        json_data = json_data
                    else:
                        self.toyaml(filename, json_data)
                        json_data = copy.deepcopy(self.json)
                else:
                    self.toyaml(filename, json_data)

    @staticmethod
    def toyaml(filename, json_data):
        # json数据转换为yaml
        if type(json_data) is 'string':
            json_data = eval(json_data)
        # 写入yaml文件
        filepath = TESTCASE_YAML_PATH + os.sep + filename + ".yaml"
        try:
            with open(filepath, "w") as f:
                json_yaml = yaml.dump(json_data, default_flow_style=False, allow_unicode=True)
                f.write(json_yaml)
        except Exception:
            raise Exception("打开文件失败，文件路径：" + filepath)
        finally:
            f.close()



if __name__ == '__main__':
    DoExcel().excel_data()
