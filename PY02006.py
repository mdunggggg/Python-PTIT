def process():
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    A.sort()
    B.sort()
    for i in range(0 , n):
        if A[i] > B[i]:
            print("NO")
            return 
    print("YES")
    return 
for i in range(int(input())):
    process()