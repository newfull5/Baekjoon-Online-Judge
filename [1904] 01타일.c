n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a,b=1,2
    for i in range(3,n+1):
        a,b=b%15746, (a+b)%15746
    print(b%15746)
