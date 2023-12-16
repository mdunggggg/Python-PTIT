def process():
    n, a = int(input()),list(map(int, input().split()))
    st = []
    for i in range(n):
        while len(st) != 0 and a[i] >= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            print(i + 1, end=" ")
        else:
            print(i - st[-1], end=" ")
        st.append(i)
    print()
    return 
for i in range(int(input())):
    process()