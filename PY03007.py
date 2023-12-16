import re
s = ""
while True:
    try:
        x = input()
        s += x
    except:
        break
a = re.split("[.?!]", s)
for i in a:
    i = i.strip().lower().split()
    if len(i) == 0:
        continue
    i[0] = i[0][:1].upper() + i[0][1:]
    print(' '.join(i))