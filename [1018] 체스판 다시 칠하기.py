chess1 = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'
chess2 = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'

a,b = map(int, input().split())

inputs = []

for _ in range(a):
    inputs.append(input())

def compare(string):
    global chess1
    global chess2
    
    string = ''.join(string)
    cnt1 = 0
    cnt2 = 0
    for i in range(len(chess1)):
        if string[i] != chess1[i]:
            cnt1 += 1
            
    for i in range(len(chess2)):
        if string[i] != chess2[i]:
            cnt2 +=1
            
    return min(cnt1, cnt2)

a -= 7
b -= 7

temp = 64

for j in range(b):
    for i in range(a):
        k = (compare(list(map(lambda x: x[0+j:8+j], inputs[0+i:8+i]))))
        if temp > k:
            temp = k
            
print(temp)
