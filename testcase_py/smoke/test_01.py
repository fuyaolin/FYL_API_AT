# -*- coding: utf-8 -*-
import os
import pytest
import allure
from common.Data_Manager import Runcase
from common.Read_Path import TESTCASE_PY_NAME_PATH

PATH = os.path.realpath(__file__).replace("_py", "_yaml").replace(".py", ".yaml")
CASE = Runcase().case(PATH)
skip_reason = PATH + "(testcase skip)"


@allure.feature('Test_01')
class Test_01(object):
    @pytest.mark.skipif(len(CASE) == 0, reason=skip_reason)
    @pytest.mark.parametrize('case', CASE)
    @pytest.mark.package
    @pytest.mark.all
    def test_01(self, case):
        Runcase().all_run(path=PATH, case=case)


if __name__ == '__main__':
    pytest.main(['-vs', TESTCASE_PY_NAME_PATH])
