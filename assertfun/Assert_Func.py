import allure
from common.Log import Logger
from jsonpath import jsonpath


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
            "notin": self._notin,
        }

    # 遍历输入的结果
    def expected(self):
        for compare_value in self.expected_check:
            for key, value in compare_value.items():
                if key in self.rule.keys():
                    # key是运算符
                    # value包括（预期字段,预期值）
                    self.handle_values(key, value)
                else:
                    Logger().logs_file().info("预期运算符 {key} not in 'eq,ne,gt,ge,lt,le,in'".format(key=key))
                    assert key in "eq,ne,gt,ge,lt,le,in"

    def handle_values(self, key, value):
        for index in value:
            # expected_key是预期的key
            # expected_value是预期的value
            expected_key = index.split(',')[0]
            expected_value = index.split(',')[-1]
            if expected_key == ('status' or 'STATUS'):
                self.rule.get(key)(actual_value=int(self.actual_code), expect_value=int(expected_value))
            else:
                # actually_value 是预期的key 在实际返回json中的值，即实际key
                # actually_key 是预期的key 在实际返回json中jsonpath路径，即实际value
                actually_key = '$..expected_key'.format(expected_key=expected_key)
                if jsonpath(eval(self.actual_value), actually_key):
                    # 返回实际值进行比较
                    actually_value = jsonpath(eval(self.actual_value), actually_key)[0]
                    # 统一类型
                    if expected_value == "*":
                        # 预期值为*，代表对比返回参数的key
                        Logger().logs_file().debug("{expected_key} 此参数在返回值，查询成功"
                                                   .format(expected_key=expected_key))
                        assert True
                        continue
                    elif type(actually_value) is int:
                        expected_value = int(expected_value)
                    else:
                        actually_value = str(actually_value)
                        expected_value = str(expected_value)
                    # 进行比较
                    self.rule.get(key)(actual_value=actually_value, expect_value=expected_value)
                else:
                    allure.attach("{expected_key}此参数未在返回值中,实际结果{actual_value}"
                                  .format(expected_key=expected_key, actual_value=self.actual_value), "check")
                    Logger().logs_file().info("{expected_key}此参数未在返回值中,实际结果{actual_value}"
                                              .format(expected_key=expected_key, actual_value=self.actual_value))
                    assert False

    @staticmethod
    def _eq(expect_value, actual_value):
        allure_value(expect_value, actual_value)
        assert actual_value == expect_value

    @staticmethod
    def _ne(expect_value, actual_value):
        allure_value(expect_value, actual_value)
        assert actual_value != expect_value

    @staticmethod
    def _gt(expect_value, actual_value):
        allure_value(expect_value, actual_value)
        assert expect_value > actual_value

    @staticmethod
    def _ge(expect_value, actual_value):
        allure_value(expect_value, actual_value)
        assert expect_value >= actual_value

    @staticmethod
    def _lt(expect_value, actual_value):
        allure_value(expect_value, actual_value)
        assert expect_value < actual_value

    @staticmethod
    def _le(expect_value, actual_value):
        allure_value(expect_value, actual_value)
        assert expect_value <= actual_value

    @staticmethod
    def _in(expect_value, actual_value):
        allure_value(expect_value, actual_value)
        assert str(expect_value) in actual_value

    @staticmethod
    def _notin(expect_value, actual_value):
        allure_value(expect_value, actual_value)
        assert str(expect_value) not in actual_value


def allure_value(expect_value, actual_value):
    Logger().logs_file().info("actual_value:{actual_value};expect_value:{expect_value}"
                              .format(actual_value=actual_value, expect_value=expect_value))
    with allure.step("check"):
        allure.attach("预期结果：{expect_value}；实际结果：{actual_value}"
                      .format(expect_value=expect_value, actual_value=actual_value), "check")
