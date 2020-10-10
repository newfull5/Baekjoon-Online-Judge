length = int(intput())
arr = list(map(int,input().split()))

dp = [1 for i in range(length)]

for i in range(length):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
