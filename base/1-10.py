# 1 리스트에서 400, 500을 삭제하는 code
nums = [100, 200, 300, 400, 500]

nums.remove(400)
nums.remove(500)

# 2 리스트 내장함수 insert 이용하여 코드 입력하기
l = [200, 100, 300]
l.insert(2,10000)
print(l)

# 3 - 3

# 4 - 3

# 5 - 4

# 6 - 2

# 7 - 3, 5

# 8 - 78

# 9

year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day,sep='/', end=' ')
print(hour, minute, second, sep=':')

#10
num = int(input('별: '))
for i in range(num) :
    print(' ' * (num-(i+1))+'*'*(2*i + 1))
