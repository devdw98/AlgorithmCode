# 거스름돈
def solution(n):
    result = 0 # 동전 개수
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        result += (n // coin)
        n = n % coin
    
    return result

print(solution(1260))