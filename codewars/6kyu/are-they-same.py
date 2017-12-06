#  https://www.codewars.com/kata/are-they-the-same/

def comp(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False
    
    array1.sort()
    array2.sort()
    
    for index,item in enumerate(array1):
        if item*item != array2[index]:
            return False
            
    return True
    