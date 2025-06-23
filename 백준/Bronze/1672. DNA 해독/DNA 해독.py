import sys

input = sys.stdin.readline
dna_map = {'AA':'A', 'AG': 'C',  'AC':'A', 'AT':'G', 'GA':'C', 'GG':'G', 'GC':'T', 'GT':'A', 'CA':'A', 'CG':'T', 'CC':'C', 'CT':'G', 'TA':'G', 'TG':'A', 'TC':'G', 'TT':'T'}

n = int(input())
dna = list(input().strip())

while len(dna) > 1:
    check_dna = dna[-2] + dna[-1]
    dna.pop()
    dna[-1] = dna_map[check_dna]

print(dna[0])