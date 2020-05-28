def Solution():
    
    ropes = []
    for _ in range(int(input())):
        ropes.append(int(input()))
        
    ropes = sorted(ropes, reverse = True)
    
    temp = 0
    
    for i in range(0, len(ropes)):
        if temp < (i+1)*ropes[i]:
            temp = (i+1)*ropes[i]
        
    return temp

print(Solution())
