def Reculsive(n):
    global answer
    if n >=3:
        Reculsive(n-3)
        
    if n >=2:
        Reculsive(n-2)
        
    if n >=1:
        Reculsive(n-1)
        
    if n == 0:
        answer += 1
        return
    
for _ in range(int(input())):
    answer = 0
    Reculsive(int(input()))

    print(answer)
