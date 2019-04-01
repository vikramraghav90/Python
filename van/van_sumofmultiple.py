""" 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20."""


def sum_of_multiples(limit):
    sum = 0
    if limit < 2:
        return sum
    else:
        for i in range(limit + 1):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
    return sum




limit = int(input("<"))
print(sum_of_multiples(limit))

print(sum_of_multiples(20))
