def ShowNumbers():

###"""print all the numbers between 0 and limit 
###with a label to identify the even and odd numbers"""
    limit = int(input("Please input the limit"))
    for i in range(0,limit+1):
        if i%2 == 0:
            print ("EVEN {}".format(i))
        else:
            print ("ODD {}".format(i))
ShowNumbers()
