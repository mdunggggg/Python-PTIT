
def calc(n):
    s1 = n[0] + n[1]    
    s2 = n[n.__len__() - 2] + n[n.__len__() - 1]
    if s1 == s2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = input()
        calc(n)
        t -= 1