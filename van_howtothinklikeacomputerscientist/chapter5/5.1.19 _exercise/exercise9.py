#  Write a function that removes all occurrences of a given letter from a string
def remove_letter(letter, string):
    new_string = ""
    for item in string:
        if item == letter:
            continue
        new_string += item
    return new_string


print(remove_letter("a", "apple"))
print(remove_letter("a", "banana"))
print(remove_letter("z", "banana"))
print(remove_letter("i", "Mississippi"))
print(remove_letter("b", ""))
print(remove_letter("b", "c"))
