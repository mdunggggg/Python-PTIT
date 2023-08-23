dd = [0] * (30000 + 5)
n = int(input())
for x in input().split():
    dd[int(x)] = 1
flag = 0
for i in range(1 , n + 1):
    if dd[i] == 0 and flag == 0:
        print(i)
        flag = 1
if flag == 0:
    print(n + 1)
