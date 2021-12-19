def solution(number, k):
    answer = ''

    num_list = [x for x in number]

    tmp_list = sorted(num_list)[:k]
    for i in tmp_list:
        if i in num_list:
            num_list.remove(i)
    answer = ''.join(num_list)
    return answer

def solution1(number, k):
    answer = ''
    cnt = 0
    num_list = [x for x in number]
    # print(type(num_list[2]))
    for x in range(len(number)):
        if x+1 != len(number):
            tmp = int(number[x])
            next = int(number[x+1])
            if tmp < next:
                number[x] = ''
                cnt += 1




    return answer


if __name__ == '__main__':
    print(solution1('4177252841', 4))