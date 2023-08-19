def isPrime(n):
    if n < 2:
        return False
    for i in range(2, (int)(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def process():
    str = input()
    n = len(str)
    front = (int)(str[n - 3] + str[n - 2] + str[n - 1])
    back = (int)(str[0] + str[1] + str[2])
    if isPrime(front) and isPrime(back):
        print('YES')
    else:
        print('NO')
    return 
for i in range(int(input())):
    process()