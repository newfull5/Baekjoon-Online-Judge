"""
from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
"""

#2021.07.05
from collections import Counter

input()
arr = Counter(list(map(int, input().split())))
input()
finds = list(map(int, input().split()))
    
print(*[arr[find] for find in finds])
