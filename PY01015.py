def process():
    n = input()
    for i in range(0, len(n) - 1):
        if n[i] > n[i + 1]:
            print("NO")
            return
    print("YES")
    return 
for i in range(int(input())):
    process()