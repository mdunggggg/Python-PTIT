import math
def euler(n):
    count = n
    for i in range(2, int(math.sqrt(n)) + 1 , 1):   
        if(n % i == 0):
            while n % i == 0:
                n /= i
            count -= count // i
    if n > 1:
        count -= count // n
    return count

def isPrime(n):
    for i in range(2, int(math.sqrt(n))  + 1, 1):
        if(n % i == 0):
            return False
    return n >= 2

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        if(isPrime(euler(n))):
            print("YES")
        else:
            print("NO")

        

