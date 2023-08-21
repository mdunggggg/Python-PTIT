import math
def process():
    n = input()
    m = n[::-1]
    if math.gcd(int(n), int(m)) == 1:
        print("YES")
    else:
        print("NO")
    return 
for i in range(int(input())):
    process()