n = int(input())
a = []
while len(a) < n:
    a.extend(list(map(int, input().split())))
dd = [0] * 205
for i in a:
    dd[i] = 1
flag = 0
for i in range(1, max(a) + 1):
    if dd[i] == 0:
        print(i)
        flag = 1
if flag == 0:
    print("Excellent!")