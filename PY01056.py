def isPrime(n):
    if n < 2:
        return False
    for i in range(2, (int)(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calcSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
def process():
    n = input()
    if isPrime(calcSum(int(n))) == False:
        print('NO')
        return
    for i in range(len(n)):
        if (i % 2 != (ord(n[i]) - ord('0')) % 2):
            print('NO')
            return
    print('YES')
    return 
for i in range(int(input())):
    process()