"""

@file   : 0020-计算给定日期是那年第多少天.py

@author : xiaolu

@time   : 2019-07-01

"""
def calculate(date):
    # 1.将年月日提出来
    year, month, day = date.split('/')
    year, month, day = int(year), int(month), int(day)

    # 做一个字典  月份对应所谓的天数
    month_dict = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

    sum_day = 0
    for key in month_dict.keys():
        key = int(key)
        if key < month:
            sum_day += month_dict.get(str(key))

    sum_day += day

    # 判断当前是否为闰年  是闰年则所谓的天数上加1 否则不加
    # 闰年判断的条件   能被4整除，但不能被100整除
    if month >= 2:
        if year % 4 == 0 and year % 100 != 0:
            sum_day += 1

    print("当前日期{}是这一年的第{}天".format(date, sum_day))


if __name__ == '__main__':
    # 给定一个日期，计算时当年的第几天
    date = '2018/3/21'
    calculate(date)

