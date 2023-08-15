def tower(n, a , b , c):
    if n == 1:
        print(a, '->', c)
    else:
        tower(n - 1, a, c, b)
        print(a, '->', c)
        tower(n - 1, b, a, c)

if __name__ == '__main__':
    n = int(input())
    tower(n, 'A', 'B', 'C')