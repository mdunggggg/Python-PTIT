def process():
    n, a = int(input()), list(set(list(map(int, input().split()))))
    print(a[-1] - a[0] + 1 - len(a))
    return 
for i in range(int(input())):
    process()