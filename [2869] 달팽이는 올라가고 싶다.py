import math
import sys

a,b,v = map(int, sys.stdin.readline().split())
print(math.ceil((v-a) / (a-b)) + 1)
