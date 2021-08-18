import pytest
from common.report import Report
from common.read_path import REPORT_RESULT_PATH


if __name__ == '__main__':
    pytest.main('--alluredir={dir}'.format(dir=REPORT_RESULT_PATH), '--clean-alluredir')
