""" 4. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
- 0 EVEN
- 1 ODD
- 2 EVEN
- 3 ODD
"""


def showNumbers(limit):
    array = {}
    for item in range(limit + 1 ):
        if item % 2 == 0:
            num = item
            type_num = 'EVEN'
            array.update({num:type_num})

        else:
            num = item
            type_num = 'ODD'
            array.update({num:type_num})
    return array

limited = int(input("<"))
type = showNumbers(limited)
print(type)

print(showNumbers(0))
print(showNumbers(5))
print(f'{2+2}+{10%3}')
