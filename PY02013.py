while True:
    n = int(input())
    if n == 0:
        break
    ans = 1
    while n != 1:
        n = n / 2 if n % 2 == 0 else (n * 3 + 1)
        ans += 1
    print(ans)