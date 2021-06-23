"""
# 2020 카카오 신입 공채 - 문자열 압축
1. 문자열 길이 구하기
2. 문자열 수대로 자른 후 같은 문자가 연속적으로 있는지 보기
3. 있으면 수로 바꾸고, 없으면 넘어가기
"""


def solution(s: str):
    answer = len(s)
    for i in range(1, (len(s) // 2) + 1):  # 자르는 단위
        tmp_list = [s[j:j + i] for j in range(0, len(s), i)]
        tmp_num = 1
        tmp_str = ''
        tmp_result = ''
        for current_str in tmp_list:
            if tmp_str == current_str:
                tmp_num += 1
            else:
                tmp_result += (str(tmp_num) if tmp_num > 1 else '') + tmp_str
                tmp_str = current_str
                tmp_num = 1
        tmp_result += (str(tmp_num) if tmp_num > 1 else '') + tmp_str # 마지막 비교
        answer = min(answer, len(tmp_result))

    return answer


if __name__ == '__main__':
    result = solution("aabbccc")
    print(result)
