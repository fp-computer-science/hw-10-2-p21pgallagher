# Author: PJG (AMDG) 12/9/2020


def three_letter_words(lst):
    word_count = 0
    for x in lst:
        if len(x) == 3:
            word_count += 1
    return word_count


print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)
