while True:
    a = input()
    if a == "0":
        break
    print(a.count('0')*4 + a.count('1')*2 + (len(a) - (a.count('0') + a.count('1')))*3 + (len(a)+1))
