"""
    现存问题：
        报告的内容修改 --报告内容不满意
        返回参数中文件下载 文件/图片上传 -- 未完成未验证

        参数如何关联？随机数什么的,参数化如何调用?

        每次执行完，自动发送邮件？ --带附件得邮件调试 --执行全部测试用例

        定时执行？ --通过jenkins操作

        并发执行测试用例?初始化环境?
"""
# 运行全部用例
import os
import pytest
from common.Report import Report
from common.Read_Path import TESTCASE_PY_PATH


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

    # rp.restart()


if __name__ == '__main__':
    run_all()
