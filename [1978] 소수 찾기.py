length = int(input())

array = list(map(int, input().split()))

cnt = 0 # 소수가 아닌 것

for n in array:
    if n == 1:
        cnt += 1
        continue
    for i in range(2,n):
        if n % i == 0:
            cnt += 1
            break
            
print(length - cnt)
