def process():
    n, b = map(int, input().split())
    ans = ""
    while n > 0:
        cur = n % b;
        n //= b
        if cur < 10:
            ans += str(cur)
        else:
            ans += chr(cur - 10 + ord('A'))
    print(ans[::-1])
    return 
for i in range(int(input())):
    process()