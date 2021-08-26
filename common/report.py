# import pytest
# import allure
from common.read_path import REPORT_HTML_PATH, REPORT_RESULT_PATH


class Report(object):
    def __init__(self):
        self.result_path = REPORT_RESULT_PATH
        self.html_path = REPORT_HTML_PATH

    def get_report_url(self):
        # allure generate. / result / 5 - o. / report / 5 / --clean(指定生成报告的路径)
        rep_url = r"allure generate {result} -o {report} --clean".format(result=self.result_path, report=self.html_path)
        return rep_url

    def open_report_url(self):
        # allure open - h 127.0.0.1 - p 8888. / report / 5（启动本地服务生成链接查看报告）
        open_rep_url = r"allure open -h 127.0.0.1 - p 8888 {report}".format(report=self.html_path)
        return open_rep_url

        # allure serve 报告路径（生成HTML报告，这个会直接在线打开报告)
