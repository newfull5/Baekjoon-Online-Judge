import sys
input()

temp = list(map(int, sys.stdin.readline().split()))

print('{} {}'.format(min(temp), max(temp)))
