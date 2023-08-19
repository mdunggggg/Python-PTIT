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
    if isPrime(n) == False:
        print('NO')
        return
    prime = 0
    NotPrime = 0
    for i in str :
        if i != '2' and i != '3' and i != '5' and i != '7':
            NotPrime += 1
        else:
            prime += 1
    if prime > NotPrime:
        print('YES')
    else:
        print('NO')
    return 
for i in range(int(input())):
    process()