a,b = map(int, input().split())

arr = list(map(int, input().split()))

min_ = 1
max_ = max(arr)

while min_ <= max_:
    mid = (min_ + max_)//2
    
    answer = sum(map(lambda x: x-mid if x-mid > 0 else 0, arr)) # get_return
    
    if answer >= b:
        min_ = mid +1
    else:
        max_ = mid - 1
        
print(max_)
