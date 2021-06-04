import re


def numDifferentIntegers(word: str) -> int:
    p = re.compile('[a-z]')
    str_list = p.findall(word)
    for i in str_list:
        word = word.replace(i, '/')
    num_list = word.split('/')

    num_list = list(set(num_list))
    if '' in num_list:
        num_list.remove('')
    num_list = list(map(int, num_list))
    num_list = list(set(num_list))
    return len(num_list)


if __name__ == "__main__":
    print(numDifferentIntegers('a1b01c001'))
