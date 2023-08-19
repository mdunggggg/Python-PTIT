fibo = []
def prepare():
    fibo.append(1)
    fibo.append(1)
    for i in range(2, 93):
        fibo.append(fibo[i-1] + fibo[i-2])
prepare()
def process():
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(fibo[i - 1], end = ' ')
    print()
    return 
for i in range(int(input())):
    process()