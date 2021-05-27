# 답지봄
def solution(n: int, num_str: str):
    num_list = [int(x) for x in num_str.split(' ')]
    num_list.sort()

    target = 1
    for num in num_list:
        if target < num:
            break
        target += num

if __name__=="__main__":
    result = solution(3, '2 3 8')
    print(result)