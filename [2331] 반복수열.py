def solution(n,p):
    
    lists = []
    lists.append(n)
    before = n
    
    while True:
        num = sum(map(lambda x: int(x) ** p, list(str(before))))

        if num in lists:
            break

        lists.append(num)
        before = num

    return len(lists[:lists.index(num)])


n,p = map(int, input().split())

print(solution(n,p))
