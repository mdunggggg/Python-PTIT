
def cmp(n):
    ans = 0
    while n > 0:
        ans = ans + n % 10
        n // 10
    return ans
def process():
    n = int(input())
    list = input().split()
    list.sort(key = lambda s : (sum(int(i) for i in s), int(s)))
    print(*list)
    return 
for i in range(int(input())):
    process()