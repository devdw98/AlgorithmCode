"""
# Facebook 인터뷰
"""
def solution(S:str):
    num_result = 0
    str_list = []
    for a in list(S):
        if ord(a) - ord('A') < 0:
            num_result += int(a)
        else:
            str_list.append(a)
    str_list.sort()
    str_list.append(str(num_result))
    str_result = ''.join(str_list)
    return str_result



if __name__ == "__main__":
    print(solution("K1KA5CB7"))
    print(solution("AJKDLSI412K4JSJ9D"))