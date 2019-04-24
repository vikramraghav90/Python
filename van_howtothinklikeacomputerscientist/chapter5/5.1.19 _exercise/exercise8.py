#  Write a function that mirrors its argument
def mirror(string):
    my_string = ""
    for i in range(1, len(string)+1):
        my_string += string[-i]

    print(string+my_string)


string = input("Enter your string\n")
print(mirror(string))