def showNumbers(limit):
    for item in range(limit + 1):
        if item % 2 == 0:
            print('{0} : EVEN' .format(item))

        else:
            print('{0} : ODD'.format(item))


limited = int(input("<"))
showNumbers(limited)

