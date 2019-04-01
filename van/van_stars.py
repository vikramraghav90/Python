""" 6. Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****
"""


def show_stars(rows):
    for item in range(rows + 1):
        stars = ""
        for s in range(item):
            stars += "*"

        print(stars)


rows = int(input("<"))
print(show_stars(rows))

print(show_stars(10))
