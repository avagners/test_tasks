from datetime import datetime, timedelta


def num_1(file):
    """Сколько четных чисел в этом столбце?"""
    with open(file, "r") as file:
        data = file.readlines()
        count = 0
        for i in data:
            if int(i.strip()) % 2 == 0:
                count += 1

    print(count)


def num_2(file):
    """Сколько простых чисел в этом столбце?"""
    with open(file, "r") as file:
        data = file.readlines()
        list_int_nums = [int(i.strip()) for i in data]

    count = 0
    for i in list_int_nums:
        score_divisor = 0
        for j in range(2, i + 1):
            if i % j == 0:
                score_divisor += 1
        if score_divisor == 1:
            count += 1

    print(count)


def num_3(file):
    """Сколько чисел, меньших 0.5 в этом столбце?"""
    with open(file, "r") as file:
        data = file.readlines()
        list_float = [float(i.replace(',', '.')
                      .replace(' ', '').strip()) for i in data]

    count = 0
    for i in list_float:
        if i < 0.5:
            count += 1

    print(count)


def date_1(file):
    """Столько вторников в этом столбце?"""
    with open(file, "r") as file:
        data = file.readlines()

    count = 0
    for i in data:
        if i[:3] == 'Tue':
            count += 1

    print(count)


def date_2(file):
    """Сколько вторников в этом столбце?"""
    with open(file, "r") as file:
        data = file.readlines()

    count = 0
    for datetime_str in data:
        date = datetime_str.strip()[:10]
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        weekday = datetime.weekday(datetime_object)
        if weekday == 1:
            count += 1

    print(count)


def date_3(file):
    """Сколько последних вторников месяца в этом столбце?"""
    with open(file, "r") as file:
        data = file.readlines()
        data = [datetime.strptime(i.strip(), '%m-%d-%Y') for i in data]

    count = 0
    for date in data:
        if datetime.weekday(date) == 1:
            month_date = datetime.timetuple(date)[1]
            month_date_plus_7_days = datetime.timetuple(date + timedelta(7))[1]
            if month_date == month_date_plus_7_days:
                count += 1

    print(count)


num_1('num_1.txt')
num_2('num_2.txt')
num_3('num_3.txt')
date_1('date_1.txt')
date_2('date_2.txt')
date_3('date_3.txt')
