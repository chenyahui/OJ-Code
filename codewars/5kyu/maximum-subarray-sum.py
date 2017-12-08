# https://www.codewars.com/kata/maximum-subarray-sum
def maxSequence(arr):
    if arr is None or len(arr) == 0 :
        return 0
        
    sum,result = 0,0
    for item in arr:
        sum = (item + sum) if sum > 0 else item
        result = max(sum,result)
        
    return 0 if result < 0 else result