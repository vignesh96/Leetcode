for T in range(int(raw_input())):
    F0, F1, N = list(map(int, raw_input().strip().split()))

    for i in range(0, N):
        F0, F1 = F1, 5 * F0 + 4 * F1

    print(F0 % ((10 ** 9) + 7))