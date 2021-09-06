"""
    现存问题：
        报告的生成？
        参数如何关联？
        请求参数中文件上传 文件/图片 ？  --待学习完善
        返回参数中文件下载 文件/图片上传？
        随机数什么的,参数化如何调用?
        每次执行完，自动发送邮件？
        定时执行？ --通过jenkins操作
        执行全部测试用例 -- 报告/邮件/参数 未加入 --需修改
"""
# 运行全部用例
import os
import pytest
from common.read_path import TESTCASE_PY_PATH
# from common.report import Report
# from common.read_path import REPORT_RESULT_PATH
#
#
# if __name__ == '__main__':
#     pytest.main('--alluredir={dir}'.format(dir=REPORT_RESULT_PATH), '--clean-alluredir')


if __name__ == '__main__':
    # server中：API为单接口，smoke为冒烟
    server = ''
    model = ''
    types = 'package'
    #
    types = types if types != '' else 'all'
    model_path = TESTCASE_PY_PATH if server == '' else (TESTCASE_PY_PATH + os.sep + server if model == ''
                                                        else TESTCASE_PY_PATH + os.sep + server + os.sep + model)
    pytest.main('-v -s -m={type}'.format(type=type), model_path)
