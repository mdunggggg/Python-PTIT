def process():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = 1
    while n > 0:
        if n % 10 != 0:
            ans *= n % 10
        n //= 10
    print(ans)
    return 
for i in range(int(input())):
    process()