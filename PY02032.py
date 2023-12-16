s = input()
if len(s) % 2 != 0:
    s = s[:-1]
d = []
for i in range(0, len(s), 2):
    d.append(int(s[i:i+2]))
for i in sorted(set(d)):
    print(i, end=" ")