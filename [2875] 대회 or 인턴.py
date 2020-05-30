import math

a,b,c = map(int, input().split())

if a >= b*2:
    rest = a-(b*2)
    team = b
else:
    rest = b - (a//2)
    team = a//2

if c - rest > 0:
    team -= math.ceil((c-rest)/3)
    
print(team)
