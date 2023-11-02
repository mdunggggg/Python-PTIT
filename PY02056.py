n, m = map(int, input().split())
a = []
M = -1
for i in range(n):
    a.append(list(map(int, input().split())))
def rev(n):
    return str(n) == str(n)[::-1] and n >= 10
for i in range(n):
    for j in range(m):
        if rev(a[i][j]) == True:
            M = max(M, a[i][j])
if M == -1:
    print("NOT FOUND")
else:
    print(M)
    for i in range(n):
        for j in range(m):
            if a[i][j] == M:
                print(f"Vi tri [{i}][{j}]")



