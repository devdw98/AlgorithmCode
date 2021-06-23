# 럭키 스트레이트

def solution(num: int):
    success = "LUCKY"
    fail = "READY"

    num_str = str(num)
    num_len_half = int(len(num_str) / 2)
    left_num = num_str[:num_len_half]
    right_num = num_str[num_len_half:]

    result = [0,0]
    for i in range(num_len_half):
        result[0] = result[0] + int(left_num[i])
        result[1] = result[1] + int(right_num[i])

    if result[0] == result[1]:
        return success
    else:
        return fail

if __name__ == "__main__":
    print(solution(123402))