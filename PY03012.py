class sv:
    def __init__(self, ten, baidung, submit):
        self.ten = ten
        self.baidung = baidung
        self.submit = submit
    def __str__(self):
        return f'{self.ten} {self.baidung} {self.submit}'
a = []
for i in range(int(input())):
    x = input()
    y, z = map(int, input().split())
    a.append(sv(x, y, z))
a.sort(key=lambda x : (-x.baidung, x.submit, x.ten))
for x in a:
    print(x)
