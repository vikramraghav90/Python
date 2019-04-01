""" 7. Write a function that prints all the prime numbers between 0 and limit where limit is a parameter."""

def the_prime_numbers(limit):
    if limit < 2:
        return 0
    else:
        for item in range(2, limit):
            for i in range(2, (item//2)):
                if(item % i) == 0:
                    break
            else:
                print(item)
print(the_prime_numbers(20))



