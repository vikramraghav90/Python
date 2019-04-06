def show_stars():

###"""print all the numbers between 0 and limit 
###with a label to identify the even and odd numbers"""
    limit = int(input("Please input the limit"))
    for i in range(0,limit+1):
        for j in range(0, i+1):
            print("*",end="")
        print("\r")
show_stars()
