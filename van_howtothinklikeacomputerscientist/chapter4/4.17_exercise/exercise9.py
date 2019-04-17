def hours_in(h):
    hours = h // 3600
    return hours


def minutes_in(h):
    minutes = (h % 3600) // 60
    return minutes


def seconds_in(h):
    seconds = (h % 3600) % 60
    return seconds


print(hours_in(9010))
print(minutes_in(9010))
print(seconds_in(9010))
