def solution(n, lost, reserve):
    answer = 0
    status = [1]*n
    for i in lost:
        status[i-1] = 0
    for i in reserve:
        status[i-1] += 1
    for i in range(n):
        if status[i] == 2:

            if i == 0:
                if status[i+1] == 0:
                    status[i+1] += 1
                    status[i] -= 1
            elif i == n-1:
                if status[i-1] == 0:
                    status[i-1] += 1
                    status[i] -= 1
            else:
                if status[i-1] == 0:
                    status[i-1] += 1
                    status[i] -= 1
                elif status[i+1] == 0:
                    status[i+1] += 1
                    status[i] -= 1 

    for i in status:
        if i == 0:
            continue
        answer += 1

    return answer