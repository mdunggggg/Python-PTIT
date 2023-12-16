n, m = map(int, input().split())
a = list(map(int, input().split()))
di = {}
for i in a:
    if i in di:
        di[i] += 1
    else:
        di[i] = 0
a = sorted(di, key= lambda x : (-di[x], x))
i = 0
while i < len(a) and di[a[i]] == di[a[0]]:
    i += 1
if i == len(a):
    print("NONE")
else:
    print(a[i])