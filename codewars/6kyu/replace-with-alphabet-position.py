# https://www.codewars.com/kata/replace-with-alphabet-position
def alphabet_position(text):
    result = []
    
    bounds = [ord('A'),ord('Z'),ord('a'),ord('z')]
    
    for item in text:
        asci = ord(item)
        
        if asci <= bounds[1] and asci >= bounds[0]:
            result.append(str(asci - bounds[0] + 1))
        elif asci <= bounds[3] and asci >= bounds[2]:
            result.append(str(asci - bounds[2] + 1))
            
    return " ".join(result)