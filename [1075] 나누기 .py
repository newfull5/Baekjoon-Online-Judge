n = int(input())
f = int(input())

for i in range(0,100):
    if (((n//100)*100) + i) % f == 0:
        if i < 10:
            print(0, end='')
        print(i)
        break
