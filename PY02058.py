n, mm = map(int, input().split())
a = []
M = 0
m = 10 ** 5
for i in range(n):
    l = list(map(int, input().split()))
    M = max(M, max(l))
    m = min(m, min(l))
    a.append(l)
check = False
for i in range(n):
    for j in range(mm):
        if a[i][j] == M - m:
            check = True
            break
if check == False:
    print("NOT FOUND")
else:
    print(M - m)
    for i in range(n):
        for j in range(mm):
            if a[i][j] == M - m:
                print(f"Vi tri [{i}][{j}]")



