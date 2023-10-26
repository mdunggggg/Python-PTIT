def process():
    n, b = map(int, input().split())
    ans = ""
    while n > 0:
        t = n % b
        if t < 10:
            ans += str(t)
        else:
            ans += chr(t - 10 + ord('A'))
        n //= b
    print(ans[::-1])
    return 
for i in range(int(input())):
    process()