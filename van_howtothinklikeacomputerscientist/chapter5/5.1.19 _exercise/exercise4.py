def count_letters(word, letter):
    count = 0
    for item in word:
        if item == letter:
            count += 1
    return count


w = input("Enter the strings\n")
l = input("Enter the letter\n")
print(count_letters(w, l))