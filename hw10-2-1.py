# Author: PJG (AMDG) 12/9/2020


def count_odds(lst):
    nums_odd = 0
    for x in lst:
        if x % 2 > 0:
            nums_odd += 1
    return nums_odd


print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)
