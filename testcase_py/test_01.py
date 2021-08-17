# -*- coding: utf-8 -*-

import pytest
from common.yaml.yamlManager import ReadCase
from common.yaml.yamlParams import Params


PATH = __file__.replace("py", "yaml")
params = ReadCase(PATH).readcase()


class TestApi():
    @pytest.mark.parametrize('case', params)
    def test_01(self, case):
        Params(PATH).yaml_params_second(case)


if __name__ == '__main__':
    pytest.main(['-vs'])