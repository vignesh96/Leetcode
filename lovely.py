from itertools import permutations

for T in range(int(input())):
    cnt = 0
    s = str(input())

    if s.count('c') == 0 or s.count('h') == 0 or s.count('e') == 0 or s.count('f') == 0:
        print('normal')
        continue

    combos = [''.join(list(p)) for p in permutations("chef")]
    for i in range(len(combos)):
        if combos[i] in s:
            cnt += 1

    print("lovely " + str(cnt))