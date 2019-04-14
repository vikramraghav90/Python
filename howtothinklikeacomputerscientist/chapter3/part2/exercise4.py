numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
## (a) Write a loop that prints each of the numbers on a new line.
print("Your first output")
for numb in numbers:
    print(numb)
## (b) Write a loop that prints each number and its square on a new line.
print("Your second output")
for numb in numbers:
    print("number is ", numb," an its square is ", numb * numb)
## (c) Write a loop that adds all the numbers from the list into a variable called total. You should set the total
## variable to have the value 0 before you start adding them up, and print the value in total after the loop
## has completed.
print("Your third output")
total = 0
for numb in numbers:
    total = total + numb
print("sum of all numbers is", total)
## (d) Print the product of all the numbers in the list. (product means all multiplied together)
print("Your fourth output")
total = 1
for numb in numbers:
    total = total * numb
print("product of all numbers is", total)
