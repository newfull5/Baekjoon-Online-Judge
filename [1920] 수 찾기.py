"""
#2020.07.08
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
"""
      
#2020.12.11
input()
arr = list(map(int, input().split()))
input()
arr2 = list(map(int, input().split()))

arr.sort()

length = len(arr)

def Check(target):
    left = 0
    right = length-1
    
    if target < arr[left] or target > arr[right]:
        return 0
    
    while left <= right:

        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid -1
        elif arr[mid] < target:
            left = mid + 1

    if arr[left] == target:
        return 1
    else:
        return 0

for target in arr2:
    print(Check(target))
