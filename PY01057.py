def isPrime(n):
    if n < 2: 
        return -1
    for i in range(2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            return -1
    return 1

def process():
    n = input()
    for i in range(len(n)):
        if (isPrime(i) * isPrime(ord(n[i]) - ord('0')) == -1):
            print('NO')
            return
    print('YES')
    return 
for i in range(int(input())):
    process()