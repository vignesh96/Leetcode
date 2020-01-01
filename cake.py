def toggle(ch):
    return 'R' if ch == 'G' else 'G'


def calculate_cost(A, start_ch):
    cost = 0
    row_ch = start_ch

    for row in A:
        req_ch = row_ch
        for ch in row:
            if req_ch != ch:
                if ch == 'R':
                    cost += 5
                else:
                    cost += 3
            req_ch = toggle(req_ch)
        row_ch = toggle(row_ch)

    return cost


T = int(input())

for t in range(T):
    N, M = [int(x) for x in input().split()]
    A = [input() for _ in range(N)]

    cost = min(calculate_cost(A, 'R'), calculate_cost(A, 'G'))
    print(cost)