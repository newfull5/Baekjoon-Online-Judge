n = int(input())

cnt = 0

for i in range(1, 1000000):
    n = n - i
    cnt += 1
    
    if n <= 0:
        n += i
        break

cnt += 1

if cnt % 2 == 0:
    print('{}/{}'.format(cnt-n,n))
else:
    print('{}/{}'.format(n,cnt-n))
