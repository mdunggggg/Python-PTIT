n, m = map(int, input().split())
c = 1 if n > m else (0 if n == m else -1)
cnt = abs(n - m)
cnt2 = cnt
for i in range(n):
    a = input().split()
    if c == 1 and cnt != 0 and i % 2 == 0:
        cnt -= 1
        continue
    for j in range(m):
        if c == -1 and cnt2 != 0 and j % 2 == 1:
            cnt2 -= 1
            continue
        print(a[j], end=" ")
    cnt2 = cnt
    print()