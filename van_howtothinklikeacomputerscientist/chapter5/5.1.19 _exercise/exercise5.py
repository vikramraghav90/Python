# Your text contains 243 words, of which 109 (44.8%) contain an "e".


my_quote = """Refuse to let the pain destroy you. Don't worry about getting even. Just focus on you! Be better. Do 
better. Work harder. Become so engulfed in your own magic and success that you forget it ever happened."""

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def count(quote):
    clean_quote = ""
    count = count_letters(quote)
    for word in quote:
        if word not in punctuation:
            clean_quote += word
    sum = len(clean_quote)
    percent = round(count * 100 /sum, 1)
    print("Your text contains {} words, of which {} ({}%) contain an 'e'".format(sum, count, percent))


def count_letters(word):
    countl = 0
    for item in word:
        if item == 'e':
            countl += 1
    return countl


print(count(my_quote))
