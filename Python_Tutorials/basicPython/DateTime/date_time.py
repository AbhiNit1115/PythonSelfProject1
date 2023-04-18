# datetime: it handles date and time. It has year, month, date, hour, min, sec, ms and timezone
# info attribute
# date: it handles date without taking timezone into consideration. It has year, month and day attributes.
# time: it handles time assuming that every day has 24*60*60 secs.  hour, min, sec, ms and timezone attribute.
# timedelta: it handles duration. Duration may be difference between 2 date time or date time instances.

# Creating object of date time class:
from datetime import datetime
obj_name = datetime(2022, 1, 3, 23, 12, 3, 1)
# This will format and print the date and time as provided in the arguments. Year, Month and day are mandatory
print(obj_name)

# Date time class methods:
# now(): get current date and time and includes timezone info.
print(obj_name.now())
print()

# formatting date and time:
#strftime(): It's used to format the content of the datetime, date and time class objects. full form is
# string format to time. it converts objects into a specified format and returns the formatted string
newd1 = obj_name.strftime("%B, %d, %Y")
print(newd1)
print()

newd2 = obj_name.strftime("%d/%b/%Y")
print(newd2)
print()

newd3 = obj_name.strftime("%d-%m-%Y")
print(newd3)
print()
