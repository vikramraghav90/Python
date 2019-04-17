# Count how many words in a list have length 5

content = 'The Alchemist follows the journey of an Andalusian shepherd boy named Santiago'


words_in_list = content.split(' ')
count = 0
for item in words_in_list:
    if len(item) == 5:
        count += 1
        print(item)
    else:
        pass
print(count)

