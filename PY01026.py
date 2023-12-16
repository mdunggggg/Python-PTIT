
for i in range(int(input())):
    print(f"Test {i + 1}:", end=" ")
    if sorted(input()) == sorted(input()):
        print("YES")
    else:
        print("NO")