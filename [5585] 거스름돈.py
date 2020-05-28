changes = [500, 100, 50, 10, 5, 1]
money = 1000 - int(input())
cnt = 0

for k in changes:
    temp, money = divmod(money, k)
    cnt += temp
    
print(cnt)
