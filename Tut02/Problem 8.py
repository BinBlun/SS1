# get input
month = int(input("Enter a month from 1 to 12 : "))
day = int(input("Enter a day from 1 to 31: "))
year = int(input("Enter a year (two-digit) : "))

message = "The date " + format(month) + '/' + format(day) + '/' + format(year) + " IS "

# if else
if month * day != year:
    message += "NOT"

message += "magic"

# display result
print(message)
