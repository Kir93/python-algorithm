dna_map = {'AA':'A', 'AG': 'C', 'AC':'A', 'AT':'G', 'GA':'C', 'GG':'G', 'GC':'T', 'GT':'A', 'CA':'A', 'CG':'T', 'CC':'C', 'CT':'G', 'TA':'G', 'TG':'A', 'TC':'G', 'TT':'T'}

n = int(input())
dna = input()

i = len(dna) - 2
r = dna[-1]

while i >= 0:
    r = dna_map[dna[i] + r]
    i -= 1

print(r)