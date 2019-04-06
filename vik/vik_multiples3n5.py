def multiple():

###"""print all the numbers between 0 and limit 
###with a label to identify the even and odd numbers"""
    limit = int(input("Please input the limit"))
    j = 0;
    for i in range(0,limit+1):
        if i%3 == 0 or i%5 == 0:
            print ("going to add {}".format(i))
            j= i+j
        else:
            pass
#        print "The sum of multiples of 3 and 5 is {}".format(i))
        print (j) 
multiple()
