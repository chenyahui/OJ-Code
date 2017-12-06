# https://www.codewars.com/kata/equal-sides-of-an-array
def find_even_index(arr):
    arr_sum = sum(arr)
    left = 0
    for index,item in enumerate(arr):
        if arr_sum - left - item  == left:
            return index
        left += item
    return -1