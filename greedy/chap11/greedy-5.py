def solution(num: int, max_weight: int, weight_str: str):
    weight_list = [int(x) for x in weight_str.split(' ')]
    tmp_list = list()
    for x in range(num):
        for y in range(x, num):
            if weight_list[x] == weight_list[y]:
                continue
            tmp_list.append((x + 1, y + 1))
    print(tmp_list)
    return len(tmp_list)


if __name__ == '__main__':
    print(solution(5, 3, '1 3 2 3 2'))
