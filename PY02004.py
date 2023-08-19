def process():
    list = map(int, input().split())
    ans = 0
    for i in range (1, len(list), 1):
        if list[i] != list[i - 1]:
            ans += 1
    print(ans)
    return 
for i in range(int(input())):
    process()