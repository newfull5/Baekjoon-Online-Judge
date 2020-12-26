a,b = map(int,input().split())

m1 = []

for _ in range(a):
    m1.append(list(map(int, input().split())))

a,b = map(int,input().split())

m2 = []

for _ in range(a):
    m2.append(list(map(int, input().split())))

m2 = list(map(list, zip(*m2)))

for num1 in m1:
    temp = []
    for num2 in m2:
        sum_ = 0
        
        for i in range(len(num2)):
            sum_ += num1[i] * num2[i]
            
        print(sum_, end=' ')
    print()
