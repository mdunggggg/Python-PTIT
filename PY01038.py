def calc(n):
    num = 0
    while 1:
        if n % 7 == 0:
            print(n)
            return
        if num > 1000:
            print(-1)
            return
        num += 1
        n = n + int(str(n)[::-1])
        
    

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        calc(n)