# -*- coding: utf-8 -*-

import pytest
from common.yamlParams import Params
from common.yamlUtil import ReadYaml

PATH = __file__.replace("py", "yaml")
value = ReadYaml(PATH).read_yaml()
case = Params(value).yaml_params_case()
skip_reason = PATH + "(testcase skip)"


# @allure.story('')
class TestApi(object):
    @pytest.mark.skipif(len(case) == 0, reason=skip_reason)
    # @allure.story('')
    @pytest.mark.parametrize('case', case)
    def test_01(self, case):
        Params(value).yaml_params_split(case)


if __name__ == '__main__':
    pytest.main(['-v'])
