N,M = map(int, input().split())
lists = list(map(int, input().split()))
answer = 0

for a in range(0,N):
    for b in range(a+1,N):
        for c in range(b+1, N):
            temp = lists[a] + lists[b] + lists[c]
                
            if answer < temp and temp <= M:
                answer = temp
            
print(answer)
