num = input()
start = num[:]
cnt = 0

while True:
    cnt += 1
    
    num = num[-1] + str(sum(map(int, list(num))))[-1]
    
    if int(num) == int(start):
        break
        
print(cnt) 
