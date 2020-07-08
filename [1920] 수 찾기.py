length = int(input())
N = list(map(int, input().split()))
input()
M = list(map(int, input().split()))

N.sort()

def Binsearch(array, target, length_bottom, length_end):
    if length_bottom > length_end:
        return False
    
    mid = (length_bottom + length_end) // 2
    
    if array[mid] < target:
        return Binsearch(array, target, mid+1, length_end)
    elif array[mid] > target:
        return Binsearch(array, target, length_bottom, mid-1)
    else:
        return True

for k in M:
    if Binsearch(N, k, 0, length-1):
        print(1)
    else:
        print(0)
