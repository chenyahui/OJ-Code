# https://www.codewars.com/kata/sum-of-pairs
def sum_pairs(ints, s):
    cached = set()
    for e in ints:
        if (s - e) in cached:
            return [s - e, e]
        cached.add(e)
    return None