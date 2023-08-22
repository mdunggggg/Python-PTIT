n = int(input())
list = [int(i) for i in input().split()]
ans = 0
for i in range (1, len(list), 1):
    if list[i] != list[i - 1]:
        ans += 1
print(ans)