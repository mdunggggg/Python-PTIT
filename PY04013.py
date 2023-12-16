from datetime import datetime
class tp:
    def __init__(self, ten, start, end, luongmua):
        self.ten = ten
        self.sum = datetime.strptime(end, '%H:%M') - datetime.strptime(start, '%H:%M')
        self.luongmua = luongmua
    def __str__(self) -> str:
        return f'{self.code} {self.ten} {(self.luongmua / (self.sum.seconds /3600)):.2f}'
a = {}
t = 1
for i in range(int(input())):
    cur = tp(input(), input(), input(), int(input()))
    if cur.ten not in a:
        cur.code = "T" + str(t).zfill(2)
        t += 1
        a[cur.ten] = cur
    else:
        a[cur.ten].sum += cur.sum
        a[cur.ten].luongmua += cur.luongmua
for key, val in a.items():
    print(a[key])
        