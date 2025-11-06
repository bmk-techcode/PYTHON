# Program to display future leap years from current year to final year (automatical date)

import datetime

curentyear = datetime.datetime.now().year
finalyear = int(input("Enter the final year: "))

print(f"Leap years from {curentyear} to {finalyear}:")

for year in range(curentyear, finalyear + 1):
    
    # Leap year condition
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
