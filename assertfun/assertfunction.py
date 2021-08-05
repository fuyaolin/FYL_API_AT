

class AssertResult(object):
    # def __init__(self, check, value, code):
    def __init__(self):
        # self.expected_check = check
        self.expected_check = {'eq': [{'status': 1}, {'failed': 200}, {'status': 200}], 'lt': [{'@timestamp': 2}]}
        self.actual_value = {"took": 9,
                             "timed_out": False,
                             "_shards": {"total": 303,
                                         "successful": 300,
                                         "skipped": 0,
                                         "failed": 0},
                             "hits": {
                                 "total": {
                                     "value": 10000,
                                     "relation": "gte"},
                                 "max_score": 1.0,
                                 "hits": [{
                                     "_index": "at-2021.03.29-0",
                                     "_type": "_doc",
                                     "_id": "OCG-fXgBnt4dxJOpGt08",
                                     "_score": 1.0,
                                     "_source":{
                                         "@timestamp": "2021-03-29T11:29:32.000Z",
                                         "type": "at", "host": "192.168.84.26",
                                         "tags": "AnyRobt_Test",
                                         "server": "SystemConfig"
                                     }}]}}
        # self.actual_value = value
        self.actual_code = 200
        # self.actual_code = code

    # 遍历输入的结果
    def expected(self):
        for key in self.expected_check.keys():
            if key == 'eq':
                for i in self.expected_check[key]:
                    for expected_key, expected_value in i.items():
                        print(expected_key, expected_value)
            elif key == 'lt':
                for i in self.expected_check[key]:
                    for expected_key, expected_value in i.items():
                        print(expected_key, expected_value)
            elif key == 'gt':
                for i in self.expected_check[key]:
                    for expected_key, expected_value in i.items():
                        print(expected_key, expected_value)
    #
    # # 实际返回值
    # def actual(self):
    #     pass
    #

    def compare(self, key, expected_key, expected_value):
        if key == 'eq':
            pass
        elif key == 'lt':
            pass
        elif key == 'gt':
            pass


if __name__ == '__main__':
    AssertResult().expected()
