from datetime import datetime
class gamer:
    def __init__(self, code, name, start, end):
        self.code = code
        self.name = name
        self.time = datetime.strptime(end, '%H:%M') - datetime.strptime(start, '%H:%M') 
    def __str__(self) -> str:
        return f'{self.code} {self.name} {self.time.seconds // 3600} gio {self.time.seconds % 3600 // 60} phut'
a = []
for i in range(int(input())):
    a.append(gamer(input(), input(), input(), input()))
a.sort(key=lambda x : -x.time.seconds)
for i in a:
    print(i)