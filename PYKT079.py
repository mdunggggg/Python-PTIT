def process():
    n, a = int(input()), list(map(int, input().split()))
    M = max(a)
    m = min(a)
    c = 0
    for i in range(m , M + 1, 1):
        if i not in a: 
            c += 1
    print(c)
    return 
for i in range(int(input())):
    process()