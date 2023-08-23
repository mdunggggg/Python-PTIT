def process():
    dd = [0] * (1000000+ 5)
    n = int(input())
    list = [int(x) for x in input().split()]
    for x in list:
        dd[int(x)] += 1
    list.sort()
    for i in list:
        if dd[i] > n / 2:
            print(i)
            return
    print("NO")
for i in range(int(input())):
    process()