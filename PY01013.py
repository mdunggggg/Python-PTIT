import math
def sum(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n //= 10
    return ans
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            return False
    return True
def process():
    a, b = map(int, input().split())
    if isPrime(sum(math.gcd(a, b))) == True:
        print("YES")
    else:
        print("NO")
    return 
for i in range(int(input())):
    process()