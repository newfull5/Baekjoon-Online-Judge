a = int(input())
b = int(input())

array = []

for i in range(a,b+1):
    if i < 2:
        continue
    array.append(i)
    for j in range(2,i):
        if i % j == 0:
            array.pop()
            break 

if not array:
    print('-1')
else:
    print(sum(array))
    print(array[0])
