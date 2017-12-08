def to_camel_case(text):
    should_capitalize = False
    result = ""
    for item in text:
        if should_capitalize:
            result += item.upper()
            should_capitalize = False
        elif item == '-' or item == '_':
            should_capitalize = True
        else :
             result += item
        
    return result