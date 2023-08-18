import math
for t in range(int(input())):
    n, x, m = map(float, input().split())
    print(math.ceil(math.log(m / n, 1 + x / 100)))