"""

每1秒print 一次
跑1分鐘就結束

"""

import time
import names


def one1(endSec):
    for i in range(1, endSec):
        # print(i)
        time_formatted = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        # print(time.time())  # epoch time
        # print(time.localtime(time.time()))  # localtime time
        # # time.struct_time(tm_year=2021, tm_mon=12, tm_mday=12, tm_hour=13, tm_min=37, tm_sec=15, tm_wday=6, tm_yday=346, tm_isdst
        print(time_formatted)
        print(names.get_full_name())

        time.sleep(1)

    time_formatted_stop = time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('program stop at %s' % (time_formatted_stop))


# one1(10)


how_many_seconds = int(input("程式想要跑幾秒? "))
one1(how_many_seconds)
