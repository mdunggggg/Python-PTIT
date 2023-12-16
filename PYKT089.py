n, a = int(input()), []
while True:
    try:
        a.extend(list(map(int, input().split())))
    except:
        break
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
i, j = 0, len(odd) - 1
for x in a:
    if x % 2 == 0:
        print(even[i], end = ' ')
        i += 1
    else:
        print(odd[j], end = ' ')
        j -= 1