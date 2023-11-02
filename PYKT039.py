def process():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a)
    b = sorted(b)
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            return
    print("YES")
    return 
for i in range(int(input())):
    process()