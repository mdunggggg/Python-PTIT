def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            return 0;
    return 1

n , m = map(int , input().split())
for i in range(0, n):
    list = [isPrime(int(x)) for x in input().split()]
    print(*list)