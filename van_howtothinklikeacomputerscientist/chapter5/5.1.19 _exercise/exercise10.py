#   Write a function that recognizes palindrome
def reverse(string):
    my_string = ""
    for i in range(1, len(string)+1):
        my_string += string[-i]
    return my_string


def is_palindrome(string):
    if string == reverse(string):
        return True
    return False


# st = input("Enter your string\n")
# print(is_palindrome(st))
print(is_palindrome("abba"))
print(is_palindrome("tenet"))
print(is_palindrome("straw warts"))
print(not is_palindrome("banana"))
print(not is_palindrome("abab"))