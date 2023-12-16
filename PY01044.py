n, m = input().split(), input().split()
z, t = set(), set()
for i in n:
    z.add(i.lower())
    for j in m:
        if i.lower() == j.lower():
            t.add(i.lower())

for i in m:
    z.add(i.lower())
print(' '.join(sorted(z)))
print(' '.join(sorted(t)))
