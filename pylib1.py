#Python Library Code #1: Arrow Library 


import arrow

#Simple program using the arrow library to showcase the year, month, and date value from the current datetime, and using the built in functions to replace certain values with that of a specific date.


a = arrow.utcnow() #Declaring a variable for the current date/time


#Printing the current day/time
print("Year:")
print(a.year)
print("\nMonth:")
print(a.month)
print("\nDate:")
print(a.day)


#Printing current day/time and replacing it with that of 12/25/21.
print("Current date and time:")
print(a)
print("\nReplace hour and minute with 5 and 35:")
print(a.replace(hour=5, minute=35))
print("\nReplace day with 25:")
print(a.replace(day=25))
print("\nReplace year with 2021:")
print(a.replace(year=2021))
print("\nReplace month with 12:")
print(a.replace(month=12)) 
print("\nReplace timezone with 'US/Pacific:")
print(a.replace(tzinfo='US/Pacific'))