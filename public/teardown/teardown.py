from common.log import Logger

def tear_fun():
    Logger().logs_file().debug("teardown")
