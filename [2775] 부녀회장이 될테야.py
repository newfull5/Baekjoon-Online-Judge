for _ in range(int(input())):
    k = int(input())
    n = int(input())

    array = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]

    for j in range(0, 14):
        temp = []
        for i in range(1, 15):
            temp.append(sum(array[j][:i]))
        array.append(temp)
        
    print(array[k][n-1])
