def isPrime(n):
    if n < 2:
        return False
    for i in range(2 , int(n ** 0.5) + 1 , 1):
        if n % i == 0:
            return False
    return True
def process():
    n = input()
    if isPrime(int(n)) == False or isPrime(int(n[::-1])) == False:
        print("No")
        return
    ans = 0
    for i in n:
        if isPrime(int(i)) == False:
            print("No")
            return
        ans += int(i)
    if isPrime(ans) == False:
        print("No")
    else:
        print("Yes")
        
    return 
for i in range(int(input())):
    process()