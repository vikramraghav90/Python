# Write a function that removes the first occurrence of a string from another string:


def remove(substr, string):
    new_string = ""
    def_pos = string.find(substr)
    if def_pos >= 0:
        fnstring = string.split(string[def_pos: (len(substr) + def_pos)], 1)
        return new_string.join(fnstring)
    else:
        return string


print(remove("an", "banana"))
print(remove("cyc", "bicycle"))
print(remove("iss", "Mississippi"))
print(remove("eggs", "bicycle"))
print(remove("an", "annana"))
