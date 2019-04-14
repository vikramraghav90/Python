day_dict = {
0: 'Sunday',
1: 'Monday',
2: 'Tuesday',
3: 'Wednesday',
4: 'Thursday',
5: 'Friday',
6: 'Saturday',
}
def day():
    day_number = int(input("Enter the day number between 0 to 6"))
    print("your day is ",day_dict[day_number])
day()
