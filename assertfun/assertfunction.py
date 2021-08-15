import jsonpath
import numpy as np

class AssertResult(object):
    def __init__(self, check, value, code):
        self.expected_check = check
        self.actual_value = value
        self.actual_code = code
        self.rule = {
            "eq": self._eq,
            "ne": self._ne,
            "gt": self._gt,
            "ge": self._ge,
            "lt": self._lt,
            "le": self._le,
            "in": self._in,
        }

    # 遍历输入的结果
    def expected(self):
        for comparevalue in self.expected_check:
            for key, value in comparevalue.items():
                if key in self.rule.keys():
                    self.handle_values(key, value)
                else:
                    assert key in "eq,ne,gt,ge,lt,le,in"

    def handle_values(self, key, value):
        for index in value:
            # expected_key是预期的key
            # expected_value是预期的value
            expected_key =index.split(',')[0]
            expected_value = index.split(',')[-1]
            if expected_key == ('status' or 'STATUS'):
                self.rule.get(key)(actual_value=int(self.actual_code), expect_value=int(expected_value))
            else:
                # actually_value 是预期的key 在实际返回json中的值
                # actually_key 是预期的key 在实际返回json中jsonpath路径
                actually_key = '$..' + expected_key
                actually_value = jsonpath.jsonpath(self.actual_value, actually_key)[0]
                if type(actually_value) is int:
                    expected_value = int(expected_value)
                else:
                    actually_value = str(actually_value)
                    expected_value = str(expected_value)
                self.rule.get(key)(actual_value=actually_value, expect_value=expected_value)


    @staticmethod
    def _eq(expect_value, actual_value):
        assert actual_value == expect_value

    @staticmethod
    def _ne(expect_value, actual_value):
        assert actual_value != expect_value

    @staticmethod
    def _gt(expect_value, actual_value):
        assert actual_value > expect_value

    @staticmethod
    def _ge(expect_value, actual_value):
        assert actual_value >= expect_value

    @staticmethod
    def _lt(expect_value, actual_value):
        assert actual_value < expect_value


    @staticmethod
    def _le(expect_value, actual_value):
        assert actual_value <= expect_value

    @staticmethod
    def _in(expect_value, actual_value):
        assert actual_value in expect_value