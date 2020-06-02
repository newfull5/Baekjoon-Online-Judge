a,b = map(int, input().split())

from itertools import permutations

lists = list(permutations(range(1,a+1),b))
for k in lists:
    print(str(k)[1:-1].replace(',',''))
