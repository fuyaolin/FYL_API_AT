from common.log import Logger


def setup():
    Logger().logs_file().debug("setup2")


if __name__ == '__main__':
    setup()