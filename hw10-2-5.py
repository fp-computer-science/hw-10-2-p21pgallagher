# Author: PJG (AMDG) 12/9/2020


def part_sum(lst):
    counter = 0
    for letters in lst:
        if letters % 2 == 0:
            counter += letters
        else:
            counter += 0
    return counter


print(part_sum([2, 4, 6, 8, 9]) == 20)
print(part_sum([13, 12, 10]) == 0)
print(part_sum([14, 16, 32]) == 62)