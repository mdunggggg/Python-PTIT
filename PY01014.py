a, k, n = [int(i) for i in input().split()]
Min = (int(a / k) + 1) * k - a
Max = int(n / k) * k - a
if Min <= Max:
    for i in range(Min, Max + 1, k):
        print(i, end=' ')
else:
    print(-1)