#   Write a function that counts how many times a substring occurs in a string


def count(substr, string):
    count = string.count(substr)
    return count
    # results = 0
    # sub_len = len(substr)
    # for i in range(len(string)):
    #     if string[i:i+sub_len] == substr:
    #         results += 1
    #
    # return results


print(count("an", "banana"))
print(count("ana", "banana"))
print(count("nana", "banana"))
print(count("aaa", "aaaaaa"))
print(count("an", "annana"))
print(count("is", "Mississippi"))
print(count("nanan", "banana"))
