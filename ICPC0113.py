def isPrime(n):
    if n < 2:
        return False
    for i in range(2 , int(n ** 0.5) + 1 , 1):
        if n % i == 0:
            return False
    return True

def process():
    used = []
    n = int(input())
    for i in range(13, n):
        num = str(i)
        if int(num[::-1]) < n and num != num[::-1] and isPrime(int(num)) and isPrime(int(num[::-1])) and num not in used:
            print(i, num[::-1], end=' ')
            used += [num, num[::-1]]
    print()
for i in range(int(input())):
    process()
    