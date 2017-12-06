# https://www.codewars.com/kata/sort-the-odd
def sort_array(source_array):
    flags = []
    temp = []
    for index,item in enumerate(source_array):
        if item % 2 != 0:
            flags.append(index)
            temp.append(item)
    
    for index,item in enumerate(sorted(temp)):
        source_array[flags[index]] = item
    
    return source_array