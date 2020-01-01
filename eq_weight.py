#from itertools import groupby
friend_dict = {}
for T in range(int(raw_input())):
    friends = list(map(str, raw_input().strip().split()))

    for i in range(len(friends)):
        if friends[i] not in friend_dict:
            friend_dict[friends[i]] = 1
        else:
            friend_dict[friends[i]] += 1

    if len(set(friend_dict.values())) == 1:
        print("YES")
    else:
        print("NO")

    friend_dict = {}
