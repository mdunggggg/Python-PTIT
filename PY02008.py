
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2

prime = [2]
for i in range(3, 8000, 2):
    if isPrime(i):
        prime.append(i)

n, x = list(map(int, input().split()))

print(x, end = ' ')
for i in range(n):
    print(x + prime[i], end = ' ')
    x = x + prime[i]