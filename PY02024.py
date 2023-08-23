import math
def process():
    n = int(input())
    list = input().split()
    list.sort(key = lambda s : (math.prod(int(i) for i in s), int(s)))
    print(*list)
    return 
for i in range(int(input())):
    process()