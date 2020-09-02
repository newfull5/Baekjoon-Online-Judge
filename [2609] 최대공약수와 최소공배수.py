def uclid(a,b):
    if a % b == 0:
        return b
    
    return uclid(b,a%b)

a,b = map(int,input().split())
answer = uclid(a,b)

print(answer)
print(a*b//answer)
