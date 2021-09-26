"""
    现存问题：
        报告的生成？
        参数如何关联？
        返回参数中文件下载 文件/图片上传？
        随机数什么的,参数化如何调用?
        每次执行完，自动发送邮件？ --邮件调试
        定时执行？ --通过jenkins操作
        执行全部测试用例 -- 报告/邮件/参数 未加入 --需修改
        并发执行测试用例
        初始化环境
"""
# 运行全部用例
import os
import pytest
import allure
from common.Report import Report
from common.Read_Path import TESTCASE_PY_PATH


def run_all():
    # server中：API为单接口，smoke为冒烟
    server = 'smoke'
    model = ''
    types = 'all'

    rp = Report()
    rp.del_report()

    # 执行py文件路径
    model_path = TESTCASE_PY_PATH if server == '' else (TESTCASE_PY_PATH + os.sep + server if model == ''
                                                        else TESTCASE_PY_PATH + os.sep + server + os.sep + model)

    types = types if types != '' else 'all'
    allure.tag(types)

    pytest.main(['-vs', '-m={type}'.format(type=types), model_path,
                 '--alluredir={dir}'.format(dir=rp.get_result_path())])

    rp.restart()


if __name__ == '__main__':
    run_all()
