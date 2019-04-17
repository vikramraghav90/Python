def days_in_month(month):
    if month == "February":
        return 28
    elif month in ("january", "March", "May", "July", "August", "October", "December"):
        return 31
    elif month in ("April", "June", "September", "November"):
        return 30
    else:
        return None


print(days_in_month("February"))
print(days_in_month("December"))
print(days_in_month("Van"))