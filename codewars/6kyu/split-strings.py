# https://www.codewars.com/kata/split-strings/
def solution(s):
    result = []
    temp = ""
    s += "_"
    for i,e in enumerate(s):
        if i % 2 == 0 and len(temp) != 0:
            result.append(temp)
            temp = ""
        temp += e
    
    if len(temp) == 2 :
        result.append(temp)
    return result