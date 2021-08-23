# # import pytest
# # from common.report import Report
# # from common.read_path import REPORT_RESULT_PATH
# #
# #
# # if __name__ == '__main__':
# #     pytest.main('--alluredir={dir}'.format(dir=REPORT_RESULT_PATH), '--clean-alluredir')
#
# import os
#
# os.system()

import jsonpath
actually_key = "$..entityId"
actual_value = {"entityId":41,"success":1}
print(jsonpath.jsonpath(actual_value, actually_key))