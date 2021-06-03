def solution(n: int, plan_str: str):
    plans = plan_str.split(' ')

    x = 1
    y = 1
    move_plan = {'L': -1, 'R': 1, 'U': -1, 'D': 1}

    for p in plans:
        if (y == 1 and p == 'L') or (y == n and p == 'R') or (x == 1 and p == 'U') or (x == n and p == 'D'):
            continue
        if p == 'L' or p == 'R':
            y += move_plan[p]
            continue
        if p == 'U' or p == 'D':
            x += move_plan[p]
            continue
    return x, y

if __name__ == '__main__':
    print(solution(5, 'R R R U D D'))