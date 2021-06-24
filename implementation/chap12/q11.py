"""
1. 사과 위치 표시
2. 뱀이 움직이는 곳에 사과 있는지 확인
"""


def change_head(head: int,  change: str):
    if change == 'L':
        return (head + 1) % 4
    elif change == 'D':
        return (head - 1) % 4


def solution(board_size: int, apples: int, apple_location: list, change: int, snake_changes: list):
    answer = 0
    board = [[1 if [y, x] in apple_location else 0 for x in range(board_size)] for y in range(board_size)]
    snake = [0, 0]
    snake_see = 0  # 오른쪽: 0, 위: 1, 왼쪽: 2, 아래: 3
    for change in snake_changes:
        apple_num = 0
        if snake_see == 0:  # 시선 오른쪽
            for move in range(snake[1], snake[1] + change[0]):
                if [snake[0], move] in apple_location:  # 사과 존재
                    board[snake[0]][move] = 0
                    apple_num += 1
                    continue
            snake[1] += change[0] - apple_num  # 칸 이동
            answer += snake[1]
        elif snake_see == 1: # 시선 위쪽
            for move in range(snake[0], snake[0] - change[0]):
                if [move, snake[1]] in apple_location:
                    board[move][snake[1]] = 0
                    apple_num += 1
                    continue
            snake[0] += change[0] - apple_num  # 칸 이동
            answer += snake[0]
        elif snake_see == 2: # 시선 왼쪽
            for move in range(snake[1], snake[1] - change[0]):
                if [snake[0], move] in apple_location:
                    board[snake[0]][move] = 0
                    apple_num += 1
                    continue
            snake[1] += change[0] - apple_num  # 칸 이동
            answer += snake[1]
        elif snake_see == 3: # 시선 아래
            for move in range(snake[0], snake[0] + change[0]):
                if [move, snake[1]] in apple_location:
                    board[move][snake[1]] = 0
                    apple_num += 1
                    continue
            snake[0] += change[0] - apple_num # 칸 이동
            answer += snake[0]

        snake_see = change_head(snake_see, change[1])  # 뱀 머리 방향 바꾸기

        if snake[0] > board_size :
            return answer - (snake[0] - board_size)
        elif snake[1] > board_size:
            return answer - (snake[1] - board_size)

    return answer


if __name__ == '__main__':
    result = solution(6, 3, [[3, 4], [2, 5], [5, 3]], 3, [[3, 'D'], [15, 'L'], [17, 'D']])  # 9 -> 통과
    print(result)

    result2 = solution(10, 4, [[1, 2], [1, 3], [1, 4],[1,5]], 4, [[8, 'D'], [10, 'L'], [11, 'D'], [13,'L']]) # 21
    print(result2)

    result3 = solution(10, 5, [[1,5],[1,3],[1,2],[1,6],[1,7]], 4, [[8,'D'], [10,'D'],[11,'D'],[13, 'L']]) # 13
    print(result3)