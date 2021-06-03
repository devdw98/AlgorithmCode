def solution(position: str):
    x, y = position.split(' ')
    cnt = 0
    x = ord(x) - ord('a') + 1
    y = int(y)
    move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for m in move:
        dx = x + m[0]
        dy = y + m[1]
        if dx < 1 or dy < 1 or dx > 8 or dy > 8:
            continue
        cnt += 1

    return cnt


if __name__ == '__main__':
    print(solution('a 1'))