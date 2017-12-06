# https://www.codewars.com/kata/regex-validate-pin-code
def validate_pin(pin):
    pin_len = len(pin)
    if pin_len == 4 or pin_len == 6:
        for c in pin:
            if c > '9' or c < '0':
                return False
        return True
    return False