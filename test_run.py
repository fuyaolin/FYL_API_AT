"""
    现存问题：
        报告的内容修改 --报告内容不满意
        返回参数中文件下载 文件/图片上传 -- 未完成未验证

        定时执行？ --通过jenkins操作

        并发执行测试用例?初始化环境?
"""
# 运行全部用例
import os
import pytest
from config.Send_Email import sendmail
from common.BaseReport import Report
from common.ReadPath import TESTCASE_PY_PATH


def run_all():
    # server中：API为单接口，smoke为冒烟
    server = ''
    model = ''
    types = 'all'

    rp = Report()
    rp.del_report()

    # 执行py文件路径
    model_path = TESTCASE_PY_PATH if server == '' else (TESTCASE_PY_PATH + os.sep + server if model == ''
                                                        else TESTCASE_PY_PATH + os.sep + server + os.sep + model)

    types = types if types != '' else 'all'

    pytest.main(['-vs', '-m={type}'.format(type=types), model_path,
                 '--alluredir={dir}'.format(dir=rp.get_result_path())])

    rp.restart()

    # 发送邮件
    sendmail()


if __name__ == '__main__':
    run_all()
