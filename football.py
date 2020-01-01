import operator

score_board = {}
for T in range(int(input())):
    N = int(input())
    F1, F2 = map(str, input().strip().split())

    for i in range(N):
        name, value = input().split(' ')
        value = int(value.strip())
        name = name.strip()
        score_board[name] = value

    score_board = sorted(score_board.items(), key=operator.itemgetter(1), reverse = True)

    if (F1 == score_board[0][0] or F1 == score_board[1][0]) and (F2 == score_board[0][0] or F2 == score_board[1][0]):
        print("right")
    else:
        print("wrong")

    score_board = {}
