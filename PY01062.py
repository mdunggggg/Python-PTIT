def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            return False
    return True
def process():
    n = input()
    if isPrime(len(n)) == False:
        print("NO")
        return
    prime = 0
    not_prime = 0
    for i in n:
        if isPrime(ord(i) - ord('0')) == True:
            prime += 1
        else:
            not_prime += 1
   
    if prime > not_prime:
        print("YES")
    else:
        print("NO")
    return 
for i in range(int(input())):
    process()