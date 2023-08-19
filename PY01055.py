def process():
    str = input()
    if len(str) % 2 == 0 or str[0] == str[1] or str[0] != str[len(str) - 1]:
        print('NO')
        return
    for i in range(0, len(str) - 2, 2):
        if str[i] != str[i + 2]:
            print('NO')
            return
    print('YES')
for i in range(int(input())):
    process()