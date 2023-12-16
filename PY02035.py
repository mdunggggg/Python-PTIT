s = input()
k = int(input())
if len(s) % 2 != 0:
    s = s[:-1]
d = {}
for i in range(0, len(s), 2):
    x = int(s[i:i+2])
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
flag = 1
for key, val in sorted(d.items()):
    if val >= k:
        print(key, val)
        flag = 0
print("NOT FOUND" if flag == 1 else "")