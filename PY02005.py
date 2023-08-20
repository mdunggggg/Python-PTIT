n = int(input())
list = [int(i) for i in input().split()]
ans = 0
for i in range(0, n):
    for j in range(i + 1, n):
        if list[i] > list[j]:
            ans += 1
print(ans)