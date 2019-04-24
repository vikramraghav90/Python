#  Write a function that removes all occurrences of a string from another string
def remove_all(substr, string):
    new_string = ""
    def_pos = string.find(substr)
    if def_pos >= 0:
        fnstring = string.split(string[def_pos: (len(substr) + def_pos)])
        return new_string.join(fnstring)
    else:
        return string


print(remove_all("an", "banana"))
print(remove_all("cyc", "bicycle"))
print(remove_all("iss", "Mississippi"))
print(remove_all("eggs", "bicycle"))
print(remove_all("an", "annana"))