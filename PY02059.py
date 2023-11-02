n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            return False
    return True
M = 0
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]) == True:
            M = max(M, a[i][j])
if M == 0:
    print("NOT FOUND")
else:
    print(M)
    for i in range(n):
        for j in range(m):
            if M == a[i][j]:
                print(f"Vi tri [{i}][{j}]")
