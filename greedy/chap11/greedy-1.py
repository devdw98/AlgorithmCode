def solution(num: int, horror_chart: str):
    people = [int(x) for x in horror_chart.split(' ')]
    people.sort(reverse=True)
    group_num = 0
    target = people[0]

    while target <= len(people):
        people = people[target:]
        group_num += 1
        if len(people) == 0:
            break
        target = people[0]

    return group_num


if __name__ == '__main__':
    result = solution(5, '2 3 1 2 2')
    print(result)
