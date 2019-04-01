
"""3. Write a function for checking the speed of drivers. This function should have one parameter: speed.
- If speed is less than 70, it should print “Ok”.
- Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
- If the driver gets more than 12 points, the function should print: “License suspended”  """

def speed_of_driver(speed):
    if speed <= 70:
        return 'OK'

    else:
        point = (speed - 70)//5
        if point <= 12:
            return point

        else:
            return 'license suspended'



print(speed_of_driver(55))
print(speed_of_driver(75))
print(speed_of_driver(78))
print(speed_of_driver(90))
print(speed_of_driver(135))