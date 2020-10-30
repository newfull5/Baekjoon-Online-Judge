for _ in range(int(input())):
    string = input()
    input()
    arr = input()
    arr = list(arr[1:-1].split(','))

    for k in string:
        if k == 'R':
            arr.reverse()
        if k == 'D':
            if not arr:
                print('error')
                break
            else:
                arr = arr[1:]
    else:
        print(arr)
