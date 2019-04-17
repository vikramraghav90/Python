letter = ("N", "E", "S", "W")


def turn_clockwise(n):
        index = letter.index(n)
        if index < 3:
            return letter[index + 1]
        else:
            return letter[-index + 3]


print(turn_clockwise("N"))
print(turn_clockwise("W"))