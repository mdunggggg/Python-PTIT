for t in range(int(input())):
    num = input()
    x = num[0]
    y = num[1]
    flag = 1
    for i in range(0, len(num), 2):
        if x != num[i]:
            flag = 0
            break
    if flag == 1:
        for i in range(1, len(num), 2):
            if y != num[i]:
                flag = 0
                break
    if flag == 1:
        print('YES')
    else :
        print('NO')
