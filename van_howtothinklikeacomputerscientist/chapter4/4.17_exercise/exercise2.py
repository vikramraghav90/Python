days = ("Sunday", "Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday")


def day_name(number):
    if 0 <= number <= 6:
        return days[number]
    return None


n = int(input(">>>"))
print(day_name(n))

