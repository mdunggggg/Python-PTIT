for _ in range(int(input())):
    n, m = map(int, input().split())
    anh, kernal = [], []
    sum = 0
    for i in range(n): 
        anh.append(list(map(int, input().split())))
    for i in range(3): 
        kernal.append(list(map(int, input().split())))
    for i in range(0, n - 2):
        for j in range (0, m - 2):
            for k in range(0, 3):
                for l in range(0, 3):
                    sum += anh[i + k][j + l] * kernal[k][l]
    print(sum)