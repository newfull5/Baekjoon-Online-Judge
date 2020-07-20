from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    print(sum(list(map(int,stdin.readline().split()))))
