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
    start_day_number = int(input("Enter the day number between 0 to 6"))
    print("your start day is ",day_dict[start_day_number])
    nights_stay = int(input("HOw many nights are you planning to stay"))
    no_of_weeks = float((nights_stay / 7))
    remaining_days = (nights_stay % 7)
    if (remaining_days + start_day_number) <= 6 :
        day_of_week = day_dict[(remaining_days + start_day_number)]
        print("you will return after ", no_of_weeks, "weeks, on ", day_of_week)
    else:
        day_of_week = day_dict[((remaining_days + start_day_number) % 6) - 1]
        print("you will return after ", no_of_weeks, "weeks, on ", day_of_week)
        
day()
