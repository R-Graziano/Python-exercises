def isYearLeap(year):
#
# tu código del LAB 4.1.3.6
#
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def daysInMonth(year, month):
#
# tu código del LAB 4.1.3.7
#
    monthsWith31 = [1,3,5,7,8,10,12]
    monthsWith30 = [4,6,9,11]
    
    if month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    elif month in monthsWith31:
        return 31
    elif month in monthsWith30:
        return 30
    else:
        return

def dayOfYear(year, month, day):
#
# pon tu código nuevo aquí
#
    days = [daysInMonth(year,month) for month in range(1,month)]
    days.append(day)
    return sum(days)
    
    
print(dayOfYear(2000, 12, 31))