# Author: PJG (AMDG) 12/9/2020


def word_letter_counter(a, b):
    counter = 0
    for letters in a:
        if b == letters:
            counter += 1
    return counter


print(word_letter_counter("cat", "t") == 1)
print(word_letter_counter("apple", "p") == 2)
print(word_letter_counter("supercalifragilisticexpialidocious", "i") == 7)
