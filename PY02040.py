n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i] = [int(j) for j in input().split()]
k = int(input())
up, dow = 0, 0
for i in range(n):
    for j in range(0, n - i - 1):
        up += a[i][j]
        dow += a[n - i - 1][n - j - 1]
if abs(up - dow) <= k:
    print("YES")
else:
    print("NO")
print(abs(up - dow))


