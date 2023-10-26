n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i] = [int(j) for j in input().split()]
k = int(input())
up = 0
dow = 0
for i in range(0, n):
    for j in range(0, n):
        if i > j: 
            dow += a[i][j]
        if i < j:
            up += a[i][j]
if abs(up - dow) <= k:
    print("YES")
else:
    print("NO")
print(abs(up - dow))