""" 2. Write a function called fizz_buzz that takes a number.
- If the number is divisible by 3, it should return “Fizz”.
- If it is divisible by 5, it should return “Buzz”.
- If it is divisible by both 3 and 5, it should return “FizzBuzz”.
- Otherwise, it should return the same number.
"""

def fizz_buzz (a):
    if a == 0 or type(a) != int:
        return 0
    else:
        if a % 3 == 0:
            if a % 5 == 0:
                return 'FizzBuzz'
            else: 
                return 'Fizz'
        elif a % 5 == 0:
            return 'Buzz'
        else:
            return 'Null'


print(fizz_buzz(24))
print(fizz_buzz(13))
print(fizz_buzz(15))
print(fizz_buzz(9))
print(fizz_buzz(20))
print(fizz_buzz(0))
print(fizz_buzz('string'))
