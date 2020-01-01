import re

for T in range(int(raw_input())):
    S = str(raw_input()).strip()
    X = int(raw_input())
    F = str(raw_input()).strip()
    F = list(F)
    print(F)
    F = '^([A-Z]).*$'.join(F)
    print(F)

    positions = [m.start() for m in re.finditer(F, S)]
    print(positions)
    """if len(positions) < 2:
        print("-1")
        continue

    positions = map(lambda t : (t / X) + 1, positions)
    print(' '.join(map(str, positions)))
    """