def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
list = [int(i) for i in input().split()]
dd = [0] * (1000000 + 5)
for i in list:
    dd[int(i)] += 1
for i in list:
    if isPrime(i) and dd[i] != 0:
        print(i , dd[i])
        dd[i] = 0