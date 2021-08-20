# -*- coding: utf-8 -*-

import pytest
import allure
from common.yaml.yamlParams import Params
from common.yaml.yamlUtil import ReadYaml
from common.log import Logger

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
