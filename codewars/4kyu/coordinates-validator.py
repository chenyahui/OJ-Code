# https://www.codewars.com/kata/coordinates-validator
import re
def is_valid_coordinates(coordinates):
    pattern = re.compile(r'^(-)?\d+(\.\d+)?,(\s)?(-)?\d+(\.\d+)?$')
    
    if pattern.match(coordinates):
        pieces = [abs(float(item)) for item in coordinates.split(",")]
        return pieces[0] <= 90 and pieces[1] <= 180
    return False