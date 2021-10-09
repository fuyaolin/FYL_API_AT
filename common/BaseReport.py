"""
    清除之前的报告
"""
import os
from common.ReadPath import REPORT_REPORT_PATH, REPORT_RESULT_PATH


class Report(object):
    def __init__(self):
        pass

    def get_report_path(self):
        return REPORT_REPORT_PATH

    def get_result_path(self):
        return REPORT_RESULT_PATH

    def del_report(self):
        path = self.get_result_path()
        for i in os.listdir(path):
            path_file = os.path.join(path, i)
            if os.path.isfile(path_file):
                os.remove(path_file)
            else:
                for f in os.listdir(path_file):
                    path_file2 = os.path.join(path_file, f)
                    if os.path.isfile(path_file2):
                        os.remove(path_file2)

    def restart(self):
        report_cmd = self.getResultCmd()

        # 生成测试结果
        os.popen(report_cmd)

        # 生成测试报告
        url_cmd = self.getOpenUrlCmd()
        os.popen(url_cmd)

    def getResultCmd(self):
        result_cmd = r"allure generate {result} -o {report} --clean"\
            .format(result=self.get_result_path(), report=self.get_report_path())
        return result_cmd


    def getOpenUrlCmd(self):
        openUrl_cmd = r"allure open -h 127.0.0.1 -p 8088 {report}"\
            .format(report=self.get_report_path())
        return openUrl_cmd