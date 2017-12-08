# https://www.codewars.com/kata/delete-occurrences-of-an-element-if-it-occurs-more-than-n-times/
def delete_nth(order,max_e):
    times={}
    result = []
    for item  in order:
        if times.get(item) is None:
            times[item] = 1
            result.append(item)
        elif times[item] < max_e:
            times[item] += 1
            result.append(item)
    return result