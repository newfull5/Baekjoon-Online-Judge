N = int(input())

def Solution(N):
    if N < 100:
        return N
    
    cnt = 0
    
    for num in range(100, N+1):
        num = str(num)    
        a,b,c = num[0], num[1], num[2]
        if int(a)-int(b) == int(b)-int(c):
            cnt += 1
    return cnt + 99
        
print(Solution(N))
