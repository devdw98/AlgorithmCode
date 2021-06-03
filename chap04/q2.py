def solution(n: int):
    cnt = 0

    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                time = str(h)+str(m)+str(s)
                if str(n) in time:
                    cnt += 1
    return cnt

if __name__ == '__main__':
    print(solution(5))