# 11 - 1부터 100까지 더하기
s = 0
for i in range(100):
    s += i
print(s)

# 12 - class 만들기
class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    def attack(self):
        print('파이어볼')

x = Wizard(health=545, mana=210, armor=10)
print(x.health, x.mana, x.armor)
x.attack()

# 13
planets = ['수성','금성','지구','화성','목성','토성','천왕성','해왕성','명왕성']
# seq = int(input('행성:'))
# print(planets[seq-1])

# 14
# mul = int(input('3의 배수일 때 짝!:'))
# if mul % 3 == 0:
#     print('짝')
# else:
#     print(mul)

# 15
# name = input('이름:')
# print('안녕하세요. 저는 '+name+'입니다.')

# 16
# back = input('거꾸로 출력: ')
# list = reversed(back)

# print(''.join(list))

# 17
# height = int(input('키: '))
# if height >= 150:
#     print('YES')
# else:
#     print('NO')

# 18
# arr = input('점수들:').sp

# 19
pow = input('제곱 수:').split()
result = int(pow[0])**int(pow[1])
print(result)

# 20
div = input('몫과 나머지:').split()
result1 = int(div[0]) // int(div[1])
result2 = int(div[0]) % int(div[1])
print(result1, result2,sep=" ")