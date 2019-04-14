# Write a Python program to solve the general version of the above problem.  Ask the user for the time now (inhours),
#  and ask for the number of hours to wait. Your program should output what the time will be on the clockwhen the
# alarm goes off.

in_hours = int(input("please enter hours\n"))

wait = int(input("please enter the number of hourse to wait\n"))

time_alarm = (wait % 24) + in_hours
days = wait // 24
print("the alarm will go off at", time_alarm, "after", days, "day")
