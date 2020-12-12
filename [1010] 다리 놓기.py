import math

for _ in range(int(input())):
    r, n = map(int, input().split())
    print(int(math.factorial(n) / (math.factorial(n-r) * math.factorial(r))))
