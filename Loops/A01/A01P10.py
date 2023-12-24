'''Write a code that determines wheather a given year is leap or not'''
year = int(input("Enter required year: "))

if (year%4 == 0 and year % 100!= 0) or (year % 400 == 0):
    print("Given year is leap year.")
else:
    print("Given year is not leap")
