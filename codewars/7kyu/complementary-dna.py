#https://www.codewars.com/kata/complementary-dna

def DNA_strand(dna):
    pairs = {"A":"T","T":"A","G":"C","C":"G"}
    result = ""
    for i in range(len(dna)):
        result += pairs[dna[i]]
    return result