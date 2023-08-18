def process():
    num = input() 
    if num.count('1') + num.count('2') + num.count('0')  == len(num):
        print('YES')
    else:
        print('NO')
    return 
for i in range(int(input())):
    process()