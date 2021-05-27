def solution(num_str: str):
    num_list = [int(x) for x in num_str]
    result = 0
    for num in num_list:
        if result == 0 or num == 0:
            result += num
            continue
        result *= num

    return result


if __name__ == '__main__':
    result = solution('567')
    print(result)
