import sys
input = sys.stdin.readline

def Solution(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            return 'NO'
    return 'YES'
    
for test_case in range(int(input().strip())):
    n = int(input().strip())
    arr = [input().strip() for _ in range(n)]

    
    print(Solution(arr))
