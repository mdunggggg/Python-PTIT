from datetime import datetime
par = '06:00'
class Ts:
    def __init__(self, name, donvi, gio):
        self.name = name
        self.donvi = donvi
        self.gio = datetime.strptime(gio, '%H:%M') - datetime.strptime(par, '%H:%M')
    def getCode(self):
        dv = self.donvi.split()
        a = ""
        for i in dv:
            a += i[0]
        ten = self.name.split()
        for i in ten:
            a += i[0]
        return a
    def __str__(self) -> str:
        return f'{self.getCode()} {self.name} {self.donvi} {120 / (self.gio.seconds / 3600):.0f} Km/h'
a = []
for i in range(int(input())):
    a.append(Ts(input(), input(), input()))

for i in sorted(a, key=lambda x : -120 / (x.gio.seconds / 3600)):
    print(i)
        
