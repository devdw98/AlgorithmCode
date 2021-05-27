def solution(food_times: list, k): # 테스트케이스 1개 통과
    answer = 0
    foods_length = len(food_times)
    if sum(food_times) < k:
        return -1

    if foods_length > k:
        answer = k
    elif foods_length == k:
        answer = 1
    else:
        food_dict = dict()
        for x in range(foods_length):
            food_dict[x + 1] = food_times[x]

        min_time = min(food_dict.values())
        remain_k = k - (min_time * foods_length)
        while True:
            if remain_k > 0:
                is_zero = 0
                for key in food_dict.keys():
                    food_dict[key] -= min_time
                    if food_dict[key] == 0:
                        is_zero = key
                del food_dict[is_zero]
                remain_k -= (min_time * len(food_dict))
            elif remain_k == 0:
                answer = 1
                break
            else:
                answer = k % foods_length
                break

    return answer

def solution1(food_times: list, k):
    answer = 0
    # 중단할 시간보다 k 시간이 더 큰 경우
    if sum(food_times) < k:
        return -1
    # food_dict = dict()
    # for x in range(len(food_times)):
    #     food_dict[x+1] = food_times[x]
    min_time = min(food_times) # min(food_dict.values())
    time = k // len(food_times) # 반복할 수 있는 횟수
    remain_time = k % len(food_times)
    print(time, remain_time)
    if time <= min_time:
        # for key in food_dict.keys():
        #     food_dict[key] -= time
        # print(food_dict)
        for i in range(len(food_times)):
            food_times[i] -= time



        print(food_times)
    # else:


    return answer


if __name__ == '__main__':
    print(solution1([4, 3, 5], 8))
