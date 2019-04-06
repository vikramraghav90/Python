def prime():

###"""print all the numbers between 0 and limit 
###with a label to identify the even and odd numbers"""
    num = int(input("Please input the number"))
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                print ("number is not prime {}".format(num))
                break
            else:
                print ("number is prime {}".format(num))
    else:
        print ("number is not prime {}".format(num)) 
prime()
