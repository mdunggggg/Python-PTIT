s = input()
lower = 0
upper = 0
for i in s:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
if lower >= upper:
    print(s.lower())
else:
    print(s.upper())