def isPrime(n):
    if n < 2:
        return False
    for i in range(2, (int)(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def process():
    n = int(input());
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    if isPrime(sum):
        print('YES')
    else:
        print('NO')
    return 
for i in range(int(input())):
    process()