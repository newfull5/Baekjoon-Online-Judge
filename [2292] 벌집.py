n = int(input())
n -= 1
cnt = 0

for i in range(0,1000000000,6):
    n -= i
    cnt += 1
    if n <= 0:
        print(cnt)
        break
