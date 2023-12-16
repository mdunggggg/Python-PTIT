def isP(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2
n, a = int(input()), list(map(int , input().split()))
d = []
c = 0
vs = [0] * n
for i in a:
    if isP(i) == True:
        vs[c] = 1
        d.append(i)
    c += 1
d.sort()
j = 0
for i in range(0, n):
    if vs[i] == 0:
        print(a[i], end=" ")
    else:
        print(d[j], end=" ")
        j += 1