from itertools import permutations
x=list(permutations(input()))
print(len(x))
for i in x:
    print(''.join(i))
