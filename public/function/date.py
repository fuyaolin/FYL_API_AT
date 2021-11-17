"""
    时间计算
"""
import datetime
import time


class LocalTime(object):
    def __init__(self):
        self.local_time = time.localtime()

    # 输入格式返回值
    def formattime(self, format):
        return time.strftime(format, self.local_time)

    # 返回年月日
    def ymdtime(self):
        return time.strftime("%Y-%m-%d", self.local_time)

    # 返回时分秒
    def hmstime(self):
        return time.strftime("%H:%M:%S", self.local_time)

    # 返回年月日时分秒
    def wholetime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", self.local_time)

    # 返回当前时间戳
    def timestamp(self):
        return time.time()


class DateTime(object):
    def __init__(self):
        pass

    # 当前时间
    @staticmethod
    def nowtime():
        return datetime.datetime.now()

    # 获取前x天
    def daytimediff(self, num):
        return (datetime.datetime.now()-datetime.timedelta(days=num)).strftime("%Y-%m-%d %H:%M:%S")

    # 获取后x天
    def daytimeadd(self, num):
        return (datetime.datetime.now()+datetime.timedelta(days=num)).strftime("%Y-%m-%d %H:%M:%S")

    # 获取前x小时
    def hourtimediff(self, num):
        return (datetime.datetime.now()-datetime.timedelta(hours=num)).strftime("%Y-%m-%d %H:%M:%S")

    # 获取后x小时
    def hourtimeadd(self, num):
        return (datetime.datetime.now()+datetime.timedelta(hours=num)).strftime("%Y-%m-%d %H:%M:%S")

    # 获取前x秒
    def sectimediff(self, num):
        return (datetime.datetime.now()-datetime.timedelta(seconds=num)).strftime("%Y-%m-%d %H:%M:%S")

    # 获取后x秒
    def sectimeadd(self, num):
        return (datetime.datetime.now()+datetime.timedelta(seconds=num)).strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    print(DateTime().daytimeadd(1))
