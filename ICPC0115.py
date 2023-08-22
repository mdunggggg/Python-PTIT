import math
def process():
    n = int(input())
    m = n
    ans = 0
    while m > 0:
        ans += math.factorial(m % 10)
        m //= 10
    if ans == n:
        print("Yes")
    else:
        print("No")
    return 
for i in range(int(input())):
    process()