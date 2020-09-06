a = 0

for _ in range(5):
    temp = int(input())
    if temp < 40:
        a += 40
    else:
        a += temp
     
print(a//5)
