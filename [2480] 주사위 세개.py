a,b,c = map(int, input().split())

if a==b and b==c:
    print(a*1000 + 10000)
elif a==b or a==c or b==c:
    if a==b:
        print(100*a + 1000)
    elif a==c:
        print(100*a + 1000)
    elif b==c:
        print(100*b + 1000)
else:
    print(max(a,b,c)*100)
