n, a = int(input()), list(map(int, input().split()))
def check(a, k):
    for i in range(len(a)):
        if (a[i] // (k + 1)) + 1 > a[i] // k:
            return False
    return True
ans = 0
for i in range(min(a), 1 , -1):
    if check(a, i):
        for j in range(len(a)):
            ans += (a[j] // (i + 1)) + 1 
        print(ans)
        break
