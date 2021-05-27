# https://leetcode.com/problems/split-a-string-in-balanced-strings/

def solution(s) -> int:
    answer = 0
    count = 0
    for c in s:
        count += c == 'L'
        count -= c == 'R'
        answer += count == 0

    return answer

if __name__ == '__main__':
    result = solution('RLRRLLRLRL')
    print(result)
