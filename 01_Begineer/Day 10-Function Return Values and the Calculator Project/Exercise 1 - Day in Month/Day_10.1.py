def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(check_year, check_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    bool = is_leap_year(check_year)
    if bool and check_month == 2:
        return 29
    else:
        return month_days[check_month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
print(days_in_month(year, month))
