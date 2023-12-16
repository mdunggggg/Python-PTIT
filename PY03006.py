import re
s = ""
m = {}
for i in range(int(input())):
    s += input().lower() + " "
s = re.split("[^a-z]+", s)
for i in s:
    if i not in m:
        m[i] = 1
    else:
        m[i] += 1
ans = sorted(m, key=lambda x : (-m[x], x))
for i in ans:
    if i != '':
        print(i, m[i])