c1 = c2 = 0
for T in range(int(input())):
    N = int(input())
    cards = list(map(int, input().strip().split()))
    chef1 = sorted(cards[::2],reverse=True)
    chef2 = sorted(cards[1::2],reverse=True)
    for i in range(len(chef1)):
        if chef1[i] > chef2[i]:
            c1+=1
        elif chef1[i] < chef2[i]:
            c2+=1

    if c1 > c2:
        print("1")
    elif c1 < c2:
        print("2")
    else:
        print("draw")

    c1 = c2 = 0