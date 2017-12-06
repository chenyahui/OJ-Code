# https://www.codewars.com/kata/tribonacci-sequence
def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]