cost = 0
for T in range(int(input())):
    N, Y = list(map(int,input().strip().split()))
    S = (list(map(int,input().strip().split())))
    S = sorted(S)
    mid = len(S) / 2
    #print(Y - len((S[mid:])))
    if Y > len(S):
        print("-1")
        continue
    elif len(S[mid:]) >= Y:
        print("0")
        continue
    elif len(S[mid:]) < Y:
        if len(S[:mid]) < Y - len((S[mid:])):
            print("-1")
            continue
        else:
            needed = Y - len((S[mid:]))
            if Y - len((S[mid:])) == 1:
                print(S[mid] - S[mid - 1])
                continue
            for i in range(mid - 1, mid - needed - 1, -1):
                cost += S[mid] - S[i]

            print(cost)
            cost = 0




