a,b = map(int, input().split())

from itertools import product

lists = list(product(range(1,a+1), repeat=b))
for k in lists:
    print(str(k)[1:-1].replace(',',''))
