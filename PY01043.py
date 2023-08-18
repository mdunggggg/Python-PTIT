def isValid(s):
    if len(s) % 2 == 1 or s != s[::-1]:
        return False
    for i in s:
        if int(i) % 2 == 1:
            return False
    return True
def process():
    n = int(input())
    for i in range(22, n, 2):
        if isValid(str(i)):
            print(i, end=' ')
    print()
    return
for i in range(int(input())):
    process()