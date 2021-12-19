import itertools

def is_prime(num):
    num = int(num)
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            return True


def solution(numbers):
    answer = 0
    num_list = [x for x in numbers]
    result = list()
    for i in range(1, len(num_list)+1):
        result += list(itertools.permutations(num_list, i))

    for x in range(len(result)):
        result[x] = int(''.join(result[x]))

    result = list(set(result))

    for r in result:
        if is_prime(r):
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution('011'))