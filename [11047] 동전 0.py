N, K = list(map(int, input().split()))
cost = []
for _ in range(N):
    temp = int(input())
    if temp > K:
        break
    cost.append(temp)
    
answer = 0 
for i in range(len(cost)-1,-1,-1):
    temp, K = divmod(K, cost[i])
    answer += temp
    
print(answer)
 
