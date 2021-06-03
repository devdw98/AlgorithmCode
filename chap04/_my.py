# 눈 떠보니 코딩테스트 전 날 1번 문제

def solution():
    codes = [
        '   + -- + - + -   ',
        '   + --- + - +   ',
        '   + -- + - + -   ',
        '   + - + - + - +   '
             ]
    result = ''
    for c in range(len(codes)):
        codes[c] = codes[c].replace(' ', '')
        codes[c] = codes[c].replace('+', '1')
        codes[c] = codes[c].replace('-', '0')
        tmp = '0b'+codes[c]
        tmp = int(tmp, 2)
        result += chr(tmp)
    return result


if __name__ == '__main__':
    print(solution())