import pandas as pd
from datetime import datetime, timedelta


def num_1(df):
    """Сколько четных чисел в этом столбце?"""
    count = 0
    for i in df:
        if i % 2 == 0:
            count += 1
    print('Итог 1-й задачи:', count)


def num_2(df):
    """Сколько простых чисел в этом столбце?"""
    count = 0
    for i in df:
        score_divisor = 0
        for j in range(2, i + 1):
            if i % j == 0:
                score_divisor += 1
        if score_divisor == 1:
            count += 1

    print('Итог 2-й задачи:', count)


def num_3(df):
    """Сколько чисел, меньших 0.5 в этом столбце?"""
    count = 0
    for i in df:
        num = float(i.replace(',', '.').replace(' ', ''))
        if num < 0.5:
            count += 1

    print('Итог 3-й задачи:', count)


def date_1(df):
    """Столько вторников в этом столбце?"""
    count = 0
    for datetime_str in df:
        date = datetime_str.strip()
        try:
            datetime_object = datetime.strptime(date, '%a %b %d %H:%M:%S %Y')
        except BaseException as error:
            print(error)
        else:
            if datetime.timetuple(datetime_object)[6] == 1:
                count += 1

    print('Итог 4-й задачи:', count)


def date_2(df):
    """Столько вторников в этом столбце?"""
    count = 0
    for datetime_str in df:
        date = datetime_str[:10]
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        weekday = datetime.weekday(datetime_object)
        if weekday == 1:
            count += 1

    print('Итог 5-й задачи:', count)


def date_3(df):
    """Сколько последних вторников месяца в этом столбце?"""
    count = 0
    for date in df:
        date = datetime.strptime(date, '%m-%d-%Y')
        if datetime.weekday(date) == 1:
            month_date = datetime.timetuple(date)[1]
            month_date_plus_7_days = datetime.timetuple(date + timedelta(7))[1]
            if month_date != month_date_plus_7_days:
                count += 1

    print('Итог 6-й задачи:', count)


df = pd.read_excel('task_support.xlsx', sheet_name="Tasks")
df = df.drop(df.columns[[0]], axis=1)
df = df.drop(labels=[0], axis=0)
df["num1"] = df["num1"].astype(int)
df["num2"] = df["num2"].astype(int)

num_1(df["num1"])
num_2(df["num2"])
num_3(df["num3"])
date_1(df["date1"])
date_2(df["date2"])
date_3(df["date3"])
