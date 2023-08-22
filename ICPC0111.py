def process():
    n , d = map(int, input().split())
    list = [int(i) for i in input().split()]
    d %= n
    for i in range(d, n):
        print(list[i], end = " ")
    for i in range(0, d):
        print(list[i], end = " ")
    print()
    return 
for i in range(int(input())):
    process()