from sys import stdin
def cleanName(name: str):
    a = name.lower().split()
    for i in range(len(a)): a[i] = a[i][0].upper() + a[i][1:].lower()
    return ' '.join(a)
class User:
    def __init__(self, name, number, date):
        a = name.split()
        self.f = name[-1]
        self.s = name[:-1]
        self.name = name
        self.number = number
        self.date = date
    def __str__(self) -> str:
        return f'{self.name}: {self.number} {self.date}'
    def getS(self):
        return f'{self.name}: {self.number} {self.date}'
cur_date = ''
l = []
try: 
    f = open('SOTAY.txt', 'r')
except:
    f = stdin
lines = f.readlines()
i = 0
while i < len(lines):
    s = lines[i].strip()
    cur = s.split()
    if s.count('/') > 0:
        cur_date = cur[1:]
        l.append(User(cleanName(lines[i + 1][:-1]), lines[i + 2][:-1], *cur_date))
        i += 3
    else:
        l.append(User(cleanName(s), lines[i + 1][:-1], *cur_date))
        i += 2
l.sort(key=lambda x : (x.f, x.s))
ot = open('DIENTHOAI.txt', 'w')
for i in l:
    ot.write(i.getS() + '\n')
ot.close()
f.close()