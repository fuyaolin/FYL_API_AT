"""
    参数关联 - 存储参数（以文件为单位存储）
    case_memory_case = {
        "path": path
        "case":
        {
            "case1":{
                "header": None,
                "body": None,
                "url": None,
                "method": None,
                "response": None
            }

        }
    }
"""
case_memory = {
    "path": None,
    "case": {}
}


class MemoryCase(object):
    def __init__(self):
        self.memory_case_value = {
            "header": None,
            "url": None,
            "body": None,
            "method": None
        }
        global case_memory

    @staticmethod
    def add_memory_case_path(path):
        for key, value in case_memory.items():
            if key == 'path' and value != path:
                case_memory[key] = path
                case_memory["case"] = {}

    def add_memory_case_value(self, memory_case_key, header, body, url, method):
        self.memory_case_value['url'] = url
        self.memory_case_value['method'] = method
        self.memory_case_value['header'] = header
        self.memory_case_value['body'] = body
        case_memory['case'][memory_case_key] = self.memory_case_value

    @staticmethod
    def add_memory_case(memory_case_key, response):
        response = eval(response)
        case_memory['case'].setdefault(memory_case_key, {})['response'] = response

    @staticmethod
    def memory_case_param():
        return case_memory
