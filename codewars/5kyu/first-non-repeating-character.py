# https://www.codewars.com/kata/first-non-repeating-character

from collections import OrderedDict

def first_non_repeating_letter(string):
    
    cached = OrderedDict()
    
    for i,e in enumerate(string):
        l = e.lower()
        
        if cached.get(l) is None:
            cached[l] = ord(e)
        else:
            cached[l] = -1
    
    for k in cached:
        v = cached[k]
        if v != -1:
            return chr(v)
            
    return ""