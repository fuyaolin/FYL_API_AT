# -*- coding: utf-8 -*-

import pytest
from common.datamaneger import Runcase

PATH = __file__.replace("py", "yaml")
CASE = Runcase().case(PATH)
skip_reason = PATH + "(testcase skip)"


# @allure.story('')
class TestApi(object):
    @pytest.mark.skipif(len(CASE) == 0, reason=skip_reason)
    # @allure.story('')
    @pytest.mark.parametrize('case', CASE)
    def test_01(self, case):
        Runcase().run(path=PATH, case=case)


if __name__ == '__main__':
    pytest.main(['-v'])
