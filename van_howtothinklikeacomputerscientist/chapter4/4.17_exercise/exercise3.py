days = ("Sunday", "Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday")


def day_num(day):
    for item in days:
        if day == item:
            return days.index(item)
    return None


n = input(">>>")
print(day_num(n))


