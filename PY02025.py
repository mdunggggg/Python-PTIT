n, m = map(int, input().split())
a, b = set(sorted(list(map(int, input().split())))), set(sorted(list(map(int, input().split()))))

print(*sorted(a.intersection(b)))
print(*(sorted(a - b)))
print(*(sorted(b - a)))
