# importing the datetime module
from datetime import datetime
# Creating a date using year, month, day arguments
birthday = datetime(2019, 12, 13, 4, 12)
print("Birthday", birthday)
print(birthday.month)
print(birthday.year)
print(birthday.hour)
print(birthday.weekday()) 

# Create a date using datetime.now()
day_created = datetime.now()
print("Now", day_created)
print(day_created.month)
print(day_created.year)
print(day_created.hour)
print(day_created.weekday()) 


# subracting dates
data = datetime(2018, 1, 1) - datetime(2017, 1, 1)
print(data)

# Parsing a date using strptime
thing = 'Jan 24, 2011'
print(thing)
parsed_date = datetime.strptime(thing, '%b %d, %Y')
print(parsed_date)
# Rendering a date as a string using strftime
print(datetime.now())
new_date = datetime.strftime(datetime.now(), '%b %d, %Y')
print(new_date)