s = input()
if len(s) % 2 != 0:
    s = s[:-1]
d = []
for i in range(0, len(s), 2):
    x = int(s[i:i+2])
    if x not in d:
        d.append(x)
print(*d)