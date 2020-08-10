num = int(input())

for i in range(1,num):
    print('*'*i)
    
print('*'*num)

for i in range(num-1,0,-1):
    print('*'*i)
