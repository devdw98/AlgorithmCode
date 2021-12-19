def rotate_key(key: list, m: int):
    new_key = [[0 for y in range(m)] for x in range(m)]  # 2차원 배열 생성
    for i in range(m):
        for j in range(m):
            new_key[i][j] = key[m - 1 - j][i]
    return new_key


def make_expand_list(key, lock):
    expand_length = len(lock) + (len(key) - 1) * 2
    expand_list = [[0 for y in range(expand_length)] for x in range(expand_length)]
    start_point = len(key) - 1
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            expand_list[start_point + i][start_point + j] = lock[i][j]
    return expand_list


def check(key: list, lock: list, expand_list: list):
    # compare_count = len(key) + len(lock) - 1
    start_point_x = 0
    start_point_y = 0
    start_key_point = len(key) - 1
    # for n1 in range(compare_count):
    #     for n2 in range(compare_count):
    for k1 in range(len(key)):
        for k2 in range(len(key[k1])):
            expand_list[start_point_x + k1][start_point_y + k2] += key[k1][k2]
            # lock, key 넣은 후 검증 코드
    for l1 in range(len(key)):
        for l2 in range(len(key)):
            print('key['+str(l1)+']['+str(l2)+']='+str(expand_list[start_key_point+l1][start_key_point+l2]))
            if expand_list[start_key_point + l1][start_key_point + l2] != 1:
                return False

    return True


def solution(key, lock):
    answer = False
    key_length = len(key)
    lock_length = len(lock)

    for i in range(4):  # 키 90도로 4번 돌리기
        key = rotate_key(key, key_length)  # 키 돌리기
        expand_list = make_expand_list(key, lock)
        compare_count = len(key) + len(lock) - 1
        for n1 in range(compare_count):
            for n2 in range(compare_count):
                answer = check(key, lock, expand_list)
                print('-----------------------------------------')
                if answer == True:
                    break
    return answer


if __name__ == "__main__":
    result = solution(
        [
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 1]
        ],
        [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ]
    )
    print(result)
    # make_expand_list([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1],[1,1,1],[1,1,1]])
