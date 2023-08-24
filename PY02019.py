import math
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2

n = int(input())
list = sorted([int(i) for i in input().split()])
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if math.gcd(list[i], list[j]) == 1:
            print(str(list[i]) + " " + str(list[j]))