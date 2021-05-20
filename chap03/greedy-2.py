def solution(): 
    # n: 배열의 크기, m: 더해지는 횟수, k: 숫자를 k번 연속해서 더할 수 없음
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    
    data.sort()
    first = data[n-1]
    second = data[n-2]

    # 더해야하는 횟수
    count = int(m / (k+1))*k
    count += m % (k+1)

    result = 0
    result += (count * first)
    result += (m-count)*second
    return result

print(solution())