n , a = int(input()), sorted(list(map(int, input().split())))
print(max(a[-2]*a[-1], a[0]*a[1], a[-2]*a[-1]*a[-3], a[0]*a[1]*a[-1]))