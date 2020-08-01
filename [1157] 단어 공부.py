def answer():
    a = input()

    a = a.upper()

    if len(a) == 1:
        return a

    words = list(set(list(a)))

    diction = dict()
    for word in words:
        diction[word] = (a.count(word))

    temp = sorted(diction.values())

    if temp[-1] == temp[-2]:
        return '?'
    else:
        return (sorted(diction, key= lambda x: diction[x], reverse=True)[0])
    
    
print(answer())
