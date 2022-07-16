import itertools

a=['A','B','C']
print(list(map(''.join,itertools.permutations(a))))
print(list(map(''.join,itertools.permutations(a,2))))
print(list(map(''.join,itertools.combinations(a,2))))
