# 2.  You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3(a
# Wednesday).  You return home after 137 sleeps.  Write a general version of the program which asks for the starting
# day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

day = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Staturday")
starting_day_number = int(input("Enter number from 0 to 6 \n"))
length_of_your_stay = int(input("Enter the lenght of your stay, example 3 days \n"))

item = length_of_your_stay % 7
name_of_day = (starting_day_number + item)-7
# print (name_of_day)
print("the name of day of the week you will return on: ", day[name_of_day])


