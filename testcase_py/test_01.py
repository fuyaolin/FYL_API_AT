# -*- coding: utf-8 -*-

import pytest
from common.datamaneger import DataManager

PATH = __file__.replace("py", "yaml")
CASE = DataManager().case(PATH)
skip_reason = PATH + "(testcase skip)"


# @allure.story('')
class TestApi(object):
    @pytest.mark.skipif(len(CASE) == 0, reason=skip_reason)
    # @allure.story('')
    @pytest.mark.parametrize('case', CASE)
    def test_01(self, case):
        DataManager().run(path=PATH, case=case)


if __name__ == '__main__':
    pytest.main(['-v'])
