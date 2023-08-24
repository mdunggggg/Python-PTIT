def solve(n):
    if len(n) % 2 == 1 or n != n[::-1]:
        return
    for i in n:
        if int(i) % 2 != 0:
            return
    print(n, end= " ")
def process():
    n = int(input())
    for i in range(22, n , 2):
        solve(str(i))
    print()
    return 
for i in range(int(input())):
    process()