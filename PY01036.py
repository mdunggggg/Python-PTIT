def solveEven(n):
    ans = 0
    for i in range(2 , n + 1 , 2):
        ans += 1 / i
    print('{:.6f}'.format(ans))
def solveOdd(n):
    ans = 0
    for i in range(1 , n + 1 , 2):
        ans += 1 / i
    print('{:.6f}'.format(ans))
def process():
    n = int(input())
    if n % 2 == 0:
        solveEven(n)
    else:
        solveOdd(n)
    return 
for i in range(int(input())):
    process()