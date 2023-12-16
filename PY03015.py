def dfs(adj, vis, u):
    vis[u] = 1
    for i in adj[u]:
        if vis[i] == 0:
            dfs(adj, vis, i)
for t in range(int(input())):
    n, m = map(int, input().split())
    adj = [[]]
    for i in range(n + 5):
        adj.append([])
    for i in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    vis = [0] * (n + 5)
    ans = 1
    dinh = 0
    for i in range(1, n):
        cnt = 0
        vis = [0] * (n + 5)
        vis[i] = 1
        for j in range(1, n):
            if i != j:
                if vis[j] == 0:
                    cnt += 1
                    dfs(adj, vis, j)
        if cnt > ans:
            ans = cnt
            dinh = i
    print(dinh)

    