m = set()
with open('CONTACT.in') as fo:
    c = fo.readlines()
for i in c:
    m.add(i.strip().lower())

for i in sorted(m):
    print(i)
