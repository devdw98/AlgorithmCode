def solution(num: int):
    count = 0

    for i in range(1, num+1):
        tmp = i
        while tmp // 2 != 0:
            print(tmp)
            tmp = tmp % 2

    return count


if __name__ == '__main__':
    print(solution(6))