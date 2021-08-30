from common.log import Logger


def setup_function():
    Logger().logs_file().debug("setup1")


if __name__ == '__main__':
    setup_function()