def solution(s: str):
    num_list = [int(x) for x in s]
    tmp_list = []
    res_list = []
    for x in num_list:
        if len(tmp_list) == 0 or tmp_list[len(tmp_list)-1] == x:
            tmp_list.append(x)
            continue
        else:
            res_list.append(tmp_list)
            tmp_list = [x]
            continue
    res_list.append(tmp_list)

    zero_num = 0
    for x in res_list:
        if 0 in x:
            zero_num += 1
    one_num = len(res_list) - zero_num
    if one_num > zero_num:
        return zero_num
    else:
        return one_num


if __name__ == '__main__':
    result = solution('001100110')
    print(result)
