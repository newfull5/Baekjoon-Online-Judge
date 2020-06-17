import math

a, b = map(int, input().split())

pack, rest = float('inf'), float('inf')

for _ in range(b):
    temp1, temp2 = map(int, input().split())
    
    if temp1 < pack:
        pack = temp1
        
    if temp2 < rest:
        rest = temp2
        
        
print(min(rest*a, pack*math.ceil(a/6), (pack*divmod(a,6)[0]) + (rest*divmod(a,6)[1])))
 
