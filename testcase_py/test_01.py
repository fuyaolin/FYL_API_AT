# -*- coding: utf-8 -*-

import pytest
from public.yaml.yamlManager import ReadCase


PATH = __file__.replace("py", "yaml")
params = ReadCase(PATH).readcase()


class TestApi():
    @pytest.mark.parametrize('case', params)
    def test_01(self):
        pass
        # Params(PATH).yaml_params()


if __name__ == '__main__':
    pytest.main(['-vs'])
