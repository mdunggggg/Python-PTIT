for t in range(int(input())):
    num = input()
    if(num.count('4') + num.count('7') == len(num)):
        print('YES')
    else:
        print('NO')