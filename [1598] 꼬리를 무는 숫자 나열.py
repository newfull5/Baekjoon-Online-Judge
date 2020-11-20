x,y = map(int, input().split())

a,b = divmod(x,4)

c,d = divmod(y,4)

if b == 0:
    a -= 1
    b = 4
    
if d == 0:
    c -=1
    d = 4

print(abs(a-c) + abs(b-d))
