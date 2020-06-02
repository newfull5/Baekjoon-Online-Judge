a,b = map(int, input().split())

from itertools import combinations

lists = list(combinations(range(1,a+1),b))
for k in lists:
    print(str(k)[1:-1].replace(',',''))
