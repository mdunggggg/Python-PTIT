n = int(input())
a = []
for i in range(n):
    a.append(input())
ans = 0
for i in range(n):
    count = 0
    for j in range(n):
        if a[i][j] == 'C':
            count += 1
    if count != 0:
        ans += count * (count - 1) // 2
    count = 0
    for j in range(n):
        if a[j][i] == 'C':
            count += 1
    if count != 0:
        ans += count * (count - 1) // 2
print(ans)