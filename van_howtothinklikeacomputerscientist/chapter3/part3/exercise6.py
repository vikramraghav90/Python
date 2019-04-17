# Count how many words occur in a list up to and including the first occurrence of the word “sam”.  (What if“sam”
# does not occur?)

content = 'The Alchemist follows the journey of an Andalusian shepherd boy named Santiago sam'


words_in_list = content.split(' ')
count = 0
# if "sam" not in words_in_list:
#     for item in words_in_list:
#         count += 1
# else:
#     for item in words_in_list:
#         count += 1

for item in words_in_list:
        count += 1

print(count)


