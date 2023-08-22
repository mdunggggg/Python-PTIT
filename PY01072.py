def Try(i, arr):
    global n , k
    if len(arr) == k:
        print(*arr)
        return
    for j in range(i , n):
        Try(j + 1, arr + [list[j]])


n , k = map(int, input().split())
set = {int(i) for i in input().split()}
list = sorted(list(set))
n = len(list)
Try(0, [])