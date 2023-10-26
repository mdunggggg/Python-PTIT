m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))
dd = [[0] * n for i in range(m)]
ans = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == -1:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0: continue
                    if 0 <= i + x < m and 0 <= j + y < n and dd[i + x][j + y] == 0:
                        dd[i + x][j + y] = 1
                        ans += a[i + x][j + y]
                        
print(ans)