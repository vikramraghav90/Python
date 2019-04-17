days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")


def day_add(day, length):
    day = days.index(day)
    item = length % 7
    name_of_day = (int(day) + item) - 7
    return days[name_of_day]


# d = input("Enter day \n")
# l = int(input("Enter the length of your stay, example 3 days \n"))
# print(day_add(d,l))

print(day_add("Sunday", -1))
print(day_add("Sunday", -7))
print(day_add("Tuesday", -100))
