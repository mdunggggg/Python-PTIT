def calc(n, k):
    m = 2 ** (n - 1)
    if k == m: 
        return chr(n - 1 + ord('A'))
    if k > m:
        return calc(n - 1, m - (k - m))
    return calc(n - 1, k)
def process():
    n, k = map(int, input().split())
    print(calc(n, k))
    return 
for i in range(int(input())):
    process()