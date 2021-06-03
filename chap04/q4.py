def turn_left(d: int):
    return (d + 1) % 4

def solution(n: int, m: int, position: str, status: str):
    x, y, d = map(int, position.split(' '))

    # 육지, 바다 구분
    tmp = status.split('/')
    maps = [0 for _ in range(n)]
    for i in range(n):
        maps[i] = list(map(int, tmp[i].split(' ')))

    cnt, tmp = 1, 0
    directions = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}

    while True:
        # 왼쪽으로 돌기
        d = turn_left(d)
        # 칸 확인
        dx = x + directions[d][0]
        dy = y + directions[d][1]
        if tmp == 4:
            break
        if maps[dx][dy] > 0:  # 바다 또는 이미 가본 칸인 경우
            tmp += 1
            continue
        else:
            maps[x][y] = 2
            x, y = dx, dy  # 한 칸 전진
            cnt += 1
            tmp = 0

    return cnt


# 네 방향 모두 갈 수 없는데 어떻게 뒤로 갈 수 있나,,?

if __name__ == '__main__':
    print(solution(4, 4, '1 1 0', '1 1 1 1/1 0 0 1/1 1 0 1/1 1 1 1'))
