def Solution():
    import re

    a = input()
    q = re.compile('-')
    q = list(q.finditer(a))
    minus = 0
    
    if not q:
        return sum(map(int, a.split('+')))
    
    for i in range(0, len(q)-1):
        minus += sum(map(int, a[q[i].span()[1]:q[i+1].span()[0]].split('+')))

    minus += sum(map(int, a[q[-1].span()[1]:].split('+')))

    return (sum(map(int, a[:q[0].span()[0]].split('+'))) - minus)

print(Solution())
