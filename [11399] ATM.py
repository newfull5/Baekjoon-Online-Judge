input()
cost = list(map(int, input().split()))

cost = sorted(cost)
answer = 0

for i in range(1,len(cost)+1):
    answer += sum(cost[:i])
    
print(answer)
