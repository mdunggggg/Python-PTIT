n = input()
def solve(n):
    c = 0
    for i in n:
        if i != '6' and i != '8':
            print('NO')
            return
        if i == '8':
            c += 1
        else:
            c = 0
        if c == 3:
            print('NO')
            return
    print('YES')
solve(n)
