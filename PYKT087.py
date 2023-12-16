def process():
    n, k = map(int, input().split())
    ans = 0
    for i in range(0, 32):
        if (k >> i) & 1:
            ans += n ** i
            ans %= (10**9 + 7)
    print(ans)
    return 
for i in range(int(input())):
    process()