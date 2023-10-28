'''Write a program to take number of months and print the days in that month
INPUT: 4
Output: April is 30-day month'''

month = int(input())
if month == 2:
    print("February has 28 or 29 days")
elif month == 1:
    print("January is 31-day month")
elif month == 3:
    print("March is 31-day month")
elif month == 4:
    print("April is 30-day month")
elif month == 5:
    print("May is 31-day month")
elif month == 6:
    print("June is 30-day month")
elif month == 7:
    print("July is 31-day month")
elif month == 8:
    print("August is 31-day month")
elif month == 9:
    print("September is 30-day month")
elif month == 10:
    print("October is 31-day month")
elif month == 11:
    print("November is 30-day month")
elif month == 12:
    print("December is 31-day month")
else:
    raise ValueError
