
def count_letters(word):

    count = 0
    for _ in word:
        count += 1
    return count


w = input(">>>")
print(count_letters(w))