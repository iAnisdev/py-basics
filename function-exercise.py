days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_Leap_year(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    
    if not 1 <= month <= 12:
        return 'Invalid Month'
    elif month == 2 and is_Leap_year(year):
        return 29
    else:
        return days_per_month[month]
    

print(days_in_month(2020, 2))
print(days_in_month(2021, 2))
print(days_in_month(2020, 4))
print(days_in_month(2021, 4))
print(days_in_month(2020, 13))